!/bin/bash -l
#SBATCH --clusters=genius
#SBATCH --job-name=virtuoso_cluster
#SBATCH --account=intro_vsc37064
#SBATCH --output=virtuoso_cluster_output.log
#SBATCH --error=virtuoso_cluster_error.log
#SBATCH --partition=batch
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --mem-per-cpu=5000M
#SBATCH --time=08:00:00

# Load modules
module load Python/3.12.3-GCCcore-13.3.0
module load Virtuoso-opensource/7.2.14-GCC-13.2.0
module load monitor

# Define INI paths
VIRTUOSO_INI_MASTER="/data/leuven/370/vsc37064/virtuoso/virtuoso.ini"
VIRTUOSO_INI_SLAVE1="/data/leuven/370/vsc37064/virtuoso_slave1/virtuoso.ini"
VIRTUOSO_INI_SLAVE2="/data/leuven/370/vsc37064/virtuoso_slave2/virtuoso.ini"
VIRTUOSO_INI_SLAVE3="/data/leuven/370/vsc37064/virtuoso_slave3/virtuoso.ini"


MONITOR_FILE_MASTER="/data/leuven/370/vsc37064/virtuoso/monitor.log"
MONITOR_FILE_SLAVE1="/data/leuven/370/vsc37064/virtuoso_slave1/monitor.log"
MONITOR_FILE_SLAVE2="/data/leuven/370/vsc37064/virtuoso_slave2/monitor.log"
MONITOR_FILE_SLAVE3="/data/leuven/370/vsc37064/virtuoso_slave3/monitor.log"



QUERY_DIR="/data/leuven/370/vsc37064/sparql_examples_cluster"
RESULT_DIR="$QUERY_DIR/results"





cd /data/leuven/370/vsc37064/simulations
sleep 2

# Get the list of hostnames
NODES=($(scontrol show hostname $SLURM_NODELIST))
MASTER_NODE="${NODES[0]}"
SLAVE_NODES=("${NODES[@]:1}")

echo "Master Node: $MASTER_NODE"
echo "Slave Nodes: ${SLAVE_NODES[@]}"

# Update INI files (only master does it)
if [[ $(hostname) == "$MASTER_NODE" ]]; then
    ./updateClusterINI.sh "$MASTER_NODE" "${SLAVE_NODES[0]}" "${SLAVE_NODES[1]}" "${SLAVE_NODES[2]}"
fi

sleep 10

# Start 1 Virtuoso instance per node
srun --ntasks=4 --ntasks-per-node=1 bash -c '
    CURRENT_NODE=$(hostname)
    CURRENT_IP=$(hostname -I | cut -d" " -f1)


    echo "Running on node $CURRENT_NODE with IP $CURRENT_IP"

    if [[ "$CURRENT_NODE" == "'"$MASTER_NODE"'" ]]; then
        CONFIG_FILE="'"$VIRTUOSO_INI_MASTER"'"
	MONITOR_FILE="'"$MONITOR_FILE_MASTER"'"
        ROLE="MASTER"
    elif [[ "$CURRENT_NODE" == "'"${SLAVE_NODES[0]}"'" ]]; then
        CONFIG_FILE="'"$VIRTUOSO_INI_SLAVE1"'"
        MONITOR_FILE="'"$MONITOR_FILE_SLAVE1"'"
        ROLE="SLAVE1"
    elif [[ "$CURRENT_NODE" == "'"${SLAVE_NODES[1]}"'" ]]; then
        CONFIG_FILE="'"$VIRTUOSO_INI_SLAVE2"'"
        MONITOR_FILE="'"$MONITOR_FILE_SLAVE2"'"

        ROLE="SLAVE2"
    elif [[ "$CURRENT_NODE" == "'"${SLAVE_NODES[2]}"'" ]]; then
        CONFIG_FILE="'"$VIRTUOSO_INI_SLAVE3"'"
        MONITOR_FILE="'"$MONITOR_FILE_SLAVE3"'"
        ROLE="SLAVE3"
    else
        echo "This node ($CURRENT_NODE) is not part of the configured cluster. Exiting."
        exit 1
    fi

    echo "[$ROLE] Node $CURRENT_NODE starting Virtuoso with $CONFIG_FILE"
    virtuoso-t -c "$CONFIG_FILE" &
    sleep 180
    echo "[$ROLE] Node $CURRENT_NODE starting monitoring with $MONITOR_FILE"

    pid=$(ps aux | grep virtuoso-t | grep -v grep | awk '{print $2}')
    monitor -l "$MONITOR_FILE" -d 60 -p $pid &


    if [[ "$ROLE" == "MASTER" ]]; then
        echo "Checking cluster status from master node..."
       # isqlv 1111 dba dba <<EOF
# Repeat the whole cycle 10 times
for round in {1..10}; do
    echo "Starting round $round..."
    for file in "$QUERY_DIR"/*.txt; do
        filename=$(basename "$file")
        base="${filename%.txt}"
        result_file="$RESULT_DIR/${base}.out"
        time_file="$RESULT_DIR/${base}_time.out"

        echo "Running $file (Round $round)..."

        # Time the query
        START_TIME=$(date +%s%3N)  # milliseconds
        isqlv 1111 dba dba BLOBS=ON "$file" > temp_result.out
        END_TIME=$(date +%s%3N)

        # Save the time to time file
        echo $((END_TIME - START_TIME)) >> "$time_file"

        # Only store query result once (on first round)
        if [ "$round" -eq 1 ]; then
            echo "Result of $file:" > "$result_file"
            cat temp_result.out >> "$result_file"
        fi
    done
done

rm -f temp_result.out

sleep 3

#status('');
#EOF
#sleep 3
#	isqlv 1111 dba dba <<EOF
#status('');
#EOF
   #     sleep 5
        echo "Shutting down Virtuoso cluster..."
        isqlv 1111 dba dba <<EOF
cl_exec ('shutdown');
EOF
    fi

    echo "$ROLE ($CURRENT_NODE) done."
'
