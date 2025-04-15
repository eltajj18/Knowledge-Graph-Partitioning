Measurement description : single machine

#!/bin/bash -l
#SBATCH --clusters=genius
#SBATCH --job-name=virtuoso_cluster
#SBATCH --account=intro_vsc37064
#SBATCH --output=virtuoso_single_output.log
#SBATCH --error=virtuoso_single_error.log
#SBATCH --partition=batch
#SBATCH --nodes=1
#SBATCH --tasks-per-node=16
#SBATCH --mem-per-cpu=5000M
#SBATCH --time=08:00:00

RAM->80GB/node (For a node with 80 GB of RAM:​
NumberOfBuffers: (80 GB × 0.66) / 8 KB = 6,930,000 buffers​
MaxDirtyBuffers: Approximately 75% of NumberOfBuffers = 5,197,500 buffers)
NumberOfBuffers           = 7000000
MaxDirtyBuffers           = 5250000    
MaxCheckpointRemap = 3276800

