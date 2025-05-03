#!/bin/bash -l
#SBATCH --clusters=genius
#SBATCH --job-name=virtuoso_cluster
#SBATCH --account=intro_vsc37064
#SBATCH --output=virtuoso_cluster_output.log
#SBATCH --error=virtuoso_cluster_error.log
#SBATCH --partition=batch
#SBATCH --nodes=4
#SBATCH --tasks-per-node=16
#SBATCH --mem-per-cpu=5000M
#SBATCH --time=08:00:00

#module load Java/11.0.20
#module load koral/20210116
module load Python/3.12.3-GCCcore-13.3.0
#module load fabric/3.2.2-GCCcore-12.3.0 
module load Virtuoso-opensource/7.2.14-GCC-13.2.0


VIRTUOSO_INI_MASTER="/data/leuven/370/vsc37064/virtuoso/virtuoso.ini"
VIRTUOSO_INI_SLAVE1="/data/leuven/370/vsc37064/virtuoso_slave1/virtuoso.ini"
VIRTUOSO_INI_SLAVE2="/data/leuven/370/vsc37064/virtuoso_slave2/virtuoso.ini"
VIRTUOSO_INI_SLAVE3="/data/leuven/370/vsc37064/virtuoso_slave3/virtuoso.ini"


cd /data/leuven/370/vsc37064/simulations
./clean_lck_files.sh
sleep 3
./updateClusterINI.sh
#sleep 120
#cd scripts_2
#fab -f fabfile.py test
#./checkMasterIP.sh
#java -jar /data/leuven/370/vsc37064/koral/koral.jar master -c /data/leuven/370/vsc37064/koral/koralLocalConfig.xml &
sleep 15




# Start Virtuoso (without redirecting logs)
echo "Starting Virtuoso..."
virtuoso-t -c $VIRTUOSO_INI_MASTER &
sleep 15
echo "MASTER CONNECTED"
virtuoso-t -c $VIRTUOSO_INI_SLAVE1 &
sleep 15
echo "SLAVE1 CONNECTED"
virtuoso-t -c $VIRTUOSO_INI_SLAVE2 &
sleep 15
echo "SLAVE2 CONNECTED"
virtuoso-t -c $VIRTUOSO_INI_SLAVE3 &
sleep 15
echo "SLAVE3 CONNECTED"


##Shutdown Virtuoso
#/apps/leuven/rocky8/icelake/2023b/software/Virtuoso-opensource/7.2.14-GCC-13.2.0/bin/isqlv 1111 dba dba <<EOF
#shutdown;
#EOF

#for file in /data/leuven/370/vsc37064/sparql_examples/*.txt; do
 #   output_file="/data/leuven/370/vsc37064/sparql_examples/results/$(basename "${file%.txt}.out")"
  #  echo "Running $file..." > "$output_file"  # Add a header
   # /apps/leuven/rocky8/icelake/2023b/software/Virtuoso-opensource/7.2.14-GCC-13.2.0/bin/isqlv 1111 dba dba BLOBS=ON "$file" >> "$output_file"
#done

#sleep 3

QUERY_DIR="/data/leuven/370/vsc37064/sparql_examples"
RESULT_DIR="$QUERY_DIR/results"


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
