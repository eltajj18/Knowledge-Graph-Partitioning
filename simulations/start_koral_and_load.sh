#!/bin/bash

# -----------------------------
# CONFIGURATION
# -----------------------------

JAR_PATH="/data/leuven/370/vsc37064/koral/koral.jar"
CONFIG_FILE="/data/leuven/370/vsc37064/koral/koralLocalConfig.xml"
DATASET_FILE="/scratch/leuven/370/vsc37064/mlseaKG_RDF_Snapshots_ZIP/kaggle_1.nt"  # <-- Change this!
PARTITIONING_STRATEGY="HASH"             # e.g., HASH, VERTEX, etc.
MASTER_IP="127.0.0.1"
MASTER_PORT="4711"

# -----------------------------
# FUNCTIONAL LOGIC
# -----------------------------

# Start master
echo "Starting Koral master..."
java -jar "$JAR_PATH" master -c "$CONFIG_FILE" &

# Wait a bit to ensure master starts
sleep 3

# Start first slave
echo "Starting first Koral slave..."
java -jar "$JAR_PATH" slave -c "$CONFIG_FILE" &

# Wait a bit to avoid race condition
sleep 2

# Start second slave
echo "Starting second Koral slave..."
java -jar "$JAR_PATH" slave -c "$CONFIG_FILE" &

# Wait for all nodes to spin up
sleep 5

# Load dataset
echo "Loading dataset using Koral client..."
java -jar "$JAR_PATH" client -i "$MASTER_IP" -m "$MASTER_IP:$MASTER_PORT" load -c "$PARTITIONING_STRATEGY" "$DATASET_FILE"

echo "Koral setup complete and dataset loaded."

