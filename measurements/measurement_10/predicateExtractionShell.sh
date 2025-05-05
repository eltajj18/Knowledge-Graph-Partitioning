#!/bin/bash

INPUT_FILE="/scratch/leuven/370/vsc37064/mlseaKG_RDF_SNAPSHOTS_openml/openml_runs_merged.nt"
OUTPUT_DIR="/scratch/leuven/370/vsc37064/splitted_openml_runs_files/"

awk '
{
    predicate = $2
    gsub(/[^a-zA-Z0-9_]/, "_", predicate)
    filename = "/scratch/leuven/370/vsc37064/splitted_openml_runs_files/"  predicate ".nt"
    print $0 >> filename
}
' "$INPUT_FILE"

