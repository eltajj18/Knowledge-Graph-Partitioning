#!/bin/bash -l
#SBATCH --clusters=genius
#SBATCH --job-name=virtuoso_single_machine
#SBATCH --account=intro_vsc37064
#SBATCH --output=virtuoso_single_output.log
#SBATCH --error=virtuoso_single_error.log
#SBATCH --partition=batch
#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --cpus-per-task=16
#SBATCH --mem-per-cpu=5000M
#SBATCH --time=08:00:00

module load Python/3.12.3-GCCcore-13.3.0
module load Virtuoso-opensource/7.2.14-GCC-13.2.0
module load monitor

VIRTUOSO_INI_MASTER="/data/leuven/370/vsc37064/virtuoso_single/virtuoso.ini"

rm -rf /scratch/leuven/370/vsc37064/virtuoso_single/db/virtuoso.lck

sleep 3


# Start Virtuoso (without redirecting logs)
echo "Starting Virtuoso..."
virtuoso-t -c $VIRTUOSO_INI_MASTER &
sleep 180

QUERY_DIR="/data/leuven/370/vsc37064/sparql_examples"
RESULT_DIR="$QUERY_DIR/results"

pid=$(ps aux | grep virtuoso-t | grep -v grep | awk '{print $2}')
monitor -l /data/leuven/370/vsc37064/virtuoso_single/monitor.log -d 60 -p $pid &


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
        /apps/leuven/rocky8/icelake/2023b/software/Virtuoso-opensource/7.2.14-GCC-13.2.0/bin/isqlv 1111 dba dba BLOBS=ON "$file" > temp_result.out
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

#Shutdown Virtuoso
/apps/leuven/rocky8/icelake/2023b/software/Virtuoso-opensource/7.2.14-GCC-13.2.0/bin/isqlv 1111 dba dba <<EOF
shutdown;
EOF
echo "Done"
