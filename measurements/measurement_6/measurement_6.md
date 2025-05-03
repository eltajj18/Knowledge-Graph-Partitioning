Measurement description : single machine + named graph (6 named graphs, 1 for kaggle, 1 for pwc, 4 for openml) 

(1 task 16 cpu per node ; 1node)

 loading nt files to virtuoso_single_named_graph/db/virtuoso.db took ~2hr






loadingToVirtuoso.slurm
!/bin/bash -l
#SBATCH --clusters=wice
#SBATCH --job-name=virtuoso_bulk_load
#SBATCH --account=intro_vsc37064
#SBATCH --output=virtuoso_bulk_output.log
#SBATCH --error=virtuoso_bulk_error.log
#SBATCH --partition=bigmem
#SBATCH --nodes=1
#SBATCH --tasks-per-node=18
#SBATCH --mem-per-cpu=28000M
#SBATCH --time=10:00:00









queryVirtuosoOnSingleMachine.slurm 

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

RAM->80GB/node (For a node with 80 GB of RAM:​
NumberOfBuffers: (80 GB × 0.66) / 8 KB = 6,930,000 buffers​
MaxDirtyBuffers: Approximately 75% of NumberOfBuffers = 5,197,500 buffers)
NumberOfBuffers           = 7000000
MaxDirtyBuffers           = 5250000    
MaxCheckpointRemap = 3276800

AsyncQueueMaxThreads     = 24 -> the size of a pool of extra threads that can be used for query parallelization. This should be set to either 1.5 * the number of cores or 1.5 * the number of core threads; see which works better.

ThreadsPerQuery          = 16   -> the maximum number of threads a single query will take. This should be set to either the number of cores or the number of core threads; see which works better.



