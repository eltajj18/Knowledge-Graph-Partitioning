#!/bin/bash

INPUT_FILE="/scratch/leuven/370/vsc37064/mlseaKG_RDF_SNAPSHOTS_splitted/splitted_openml_runs_files/_http___www_w3_org_1999_02_22_rdf_syntax_ns_type_.nt"
OUTPUT_DIR="/scratch/leuven/370/vsc37064/splitted_types_openml_runs"

mkdir -p "$OUTPUT_DIR"

echo "Splitting $INPUT_FILE into files grouped by rdf:type object..."

# Extract unique object types
grep -oP '\s<[^>]+>\s\.' "$INPUT_FILE" | sort | uniq | while read -r line; do
    # Extract object IRI
    object=$(echo "$line" | awk '{print $1}')
    
    # Sanitize for filename (replace special characters)
    safe_name=$(echo "$object" | sed 's|[<>:/#]|_|g')
    
    # Create output file
    out_file="$OUTPUT_DIR/${safe_name}.nt"
    
    # Extract all lines with this object
    grep "$object" "$INPUT_FILE" >> "$out_file"
    
    echo "Written: $out_file"
done

echo "Done. Output in: $OUTPUT_DIR/"

