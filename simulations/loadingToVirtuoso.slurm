#!/bin/bash -l
#SBATCH --clusters=genius
#SBATCH --job-name=virtuoso_bulk_load
#SBATCH --account=intro_vsc37064
#SBATCH --output=virtuoso_bulk_output.log
#SBATCH --error=virtuoso_bulk_error.log
#SBATCH --partition=bigmem
#SBATCH --nodes=1
#SBATCH --tasks-per-node=18
#SBATCH --mem-per-cpu=21000M
#SBATCH --time=10:00:00

# Load Virtuoso module
module load Virtuoso-opensource/7.2.14-GCC-13.2.0

# Define paths
VIRTUOSO_DB_DIR="/scratch/leuven/370/vsc37064/virtuoso/db"
VIRTUOSO_INI="/data/leuven/370/vsc37064/virtuoso/virtuoso.ini"
DATA_DIR="/scratch/leuven/370/vsc37064/mlseaKG_RDF_Snapshots_ZIP"

# Navigate to the database directory
cd $VIRTUOSO_DB_DIR

# Start Virtuoso (without redirecting logs)
echo "Starting Virtuoso..."
virtuoso-t -c $VIRTUOSO_INI &

# Wait for Virtuoso to initialize
sleep 60

# Register RDF files and run bulk loader
/apps/leuven/rocky8/icelake/2023b/software/Virtuoso-opensource/7.2.14-GCC-13.2.0/bin/isqlv 1111 dba dba <<EOF
ld_dir('$DATA_DIR', '*.nt', NULL);
rdf_loader_run();
checkpoint;
EOF

# Wait for RDF loading to complete
sleep 120

# Check triple count to confirm successful loading
/apps/leuven/rocky8/icelake/2023b/software/Virtuoso-opensource/7.2.14-GCC-13.2.0/bin/isqlv 1111 dba dba <<EOF
SPARQL SELECT COUNT(*) WHERE { ?s ?p ?o };
EOF

# Shutdown Virtuoso after confirming data is loaded
/apps/leuven/rocky8/icelake/2023b/software/Virtuoso-opensource/7.2.14-GCC-13.2.0/bin/isqlv 1111 dba dba <<EOF
shutdown;
EOF

echo "Virtuoso bulk load completed successfully."

