Measurement description : single machine ( I queried both mine and Ioannis's queries) (queries from 44 till 53 is Ioannis's queries) (and query 26 is query 44 in the queries that I made)
(1 task 1 cpu per node ; 1node)

queryVirtuosoOnSingleMachine.slurm 
#!/bin/bash -l
#SBATCH --clusters=genius
#SBATCH --job-name=virtuoso_single_machine
#SBATCH --account=intro_vsc37064
#SBATCH --output=virtuoso_single_output.log
#SBATCH --error=virtuoso_single_error.log
#SBATCH --partition=bigmem
#SBATCH --nodes=1
#SBATCH --tasks-per-node=1
#SBATCH --mem-per-cpu=16000M
#SBATCH --time=08:00:00


RAM->16 GB/node (For a node with 16 GB of RAM:​
NumberOfBuffers: (16 GB × 0.66) / 8 KB = 1360000 buffers​
MaxDirtyBuffers: Approximately 75% of NumberOfBuffers = 1000000 buffers)

NumberOfBuffers          = 1360000
MaxDirtyBuffers          = 1000000

MaxCheckpointRemap = 3276800


(AsyncQueueMaxThreads     = 24 -> the size of a pool of extra threads that can be used for query parallelization. This should be set to either 1.5 * the number of cores or 1.5 * the number of core threads; see which works better.

ThreadsPerQuery          = 16   -> the maximum number of threads a single query will take. This should be set to either the number of cores or the number of core threads; see which works better.)
