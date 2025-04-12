#!/bin/bash

# -------------------------
# CONFIGURATION
# -------------------------


JAR_PATH="/data/leuven/370/vsc37064/koral/koral.jar"
MASTER_IP="127.0.0.1"
MASTER_PORT="4711"
QUERY_DIR="/data/leuven/370/vsc37064/virtuoso/sparql_examples"  # <-- Change this!
OUTPUT_DIR="$QUERY_DIR/results_koral"

# -------------------------
# SETUP
# -------------------------

# Create output directory if it doesn't exist

# -------------------------
# EXECUTE QUERIES
# -------------------------

for QUERY_FILE in "$QUERY_DIR"/*.txt; do
    QUERY_NAME=$(basename "$QUERY_FILE" .txt)
    OUTPUT_FILE="$OUTPUT_DIR/${QUERY_NAME}_result.txt"

    echo "Running query: $QUERY_NAME"

    java -jar "$JAR_PATH" client \
        -i "$MASTER_IP" \
        -m "$MASTER_IP:$MASTER_PORT" \
        query -q "$QUERY_FILE" > "$OUTPUT_FILE"

    echo " Saved result to: $OUTPUT_FILE"
done

echo " All queries executed."
