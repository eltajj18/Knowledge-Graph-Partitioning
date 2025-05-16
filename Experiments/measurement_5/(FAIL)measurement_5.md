easurement description : distributed machine
(1 task 16 cpu per node ; 4 nodes)
Also I added From Clause to describe which graph I was looking for
Database Replicated across all nodes

Added sleep statements, will see how it goes


loadingToVirtuosoCluster2.slurm:

#!/bin/bash -l
#SBATCH --clusters=genius
#SBATCH --job-name=virtuoso_cluster
#SBATCH --account=intro_vsc37064
#SBATCH --output=virtuoso_cluster_output.log
#SBATCH --error=virtuoso_cluster_error.log
#SBATCH --partition=batch
#SBATCH --nodes=4
#SBATCH --ntasks-per-node=1
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

