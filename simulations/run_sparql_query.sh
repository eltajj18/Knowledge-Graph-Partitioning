#!/bin/bash

# Define Virtuoso ISQL command
ISQL_CMD="/apps/leuven/rocky8/icelake/2023b/software/Virtuoso-opensource/7.2.14-GCC-13.2.0/bin/isqlv 1111 dba dba"

# Define the directory where query files are stored
QUERY_DIR="/data/leuven/370/vsc37064/virtuoso/sparql_examples"

# Define the output directory (create if it doesn't exist)
OUTPUT_DIR="$QUERY_DIR/results"


# Loop through all query files in the directory
for QUERY_FILE in "$QUERY_DIR"/*.txt; do
    # Extract filename without path
    QUERY_NAME=$(basename "$QUERY_FILE")
    OUTPUT_FILE="$OUTPUT_DIR/${QUERY_NAME%.txt}_result.txt"

    echo "Running query: $QUERY_NAME"
    
    # Execute the query and save output
    $ISQL_CMD < "$QUERY_FILE" > "$OUTPUT_FILE"

    echo "Query results saved to: $OUTPUT_FILE"
done

echo "All queries executed successfully."

