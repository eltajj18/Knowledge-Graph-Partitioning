Measurement description : 4 nodes, database replicated, individual virtuoso.ini files and cluster.ini files, 
no partitioning or indexing yet

## HARDWARE
#SBATCH --job-name=virtuoso_cluster
#SBATCH --account=intro_vsc37064
#SBATCH --output=virtuoso_cluster_output.log
#SBATCH --error=virtuoso_cluster_error.log
#SBATCH --partition=batch
#SBATCH --nodes=4
#SBATCH --tasks-per-node=16
#SBATCH --mem-per-cpu=5000M
#SBATCH --time=08:00:00


RAM->80GB/node (For a node with 80 GB of RAM:​
NumberOfBuffers: (80 GB × 0.66) / 8 KB = 6,930,000 buffers​
MaxDirtyBuffers: Approximately 75% of NumberOfBuffers = 5,197,500 buffers)
NumberOfBuffers           = 7000000
MaxDirtyBuffers           = 5250000    
Problem with this though: the server starts but I can't start ISQL so I had to lower the amount of NumberOfBuffers and MaxDirtyBuffers
; Uncomment next two lines if there is 16 GB system memory free
NumberOfBuffers          = 1360000
MaxDirtyBuffers          = 1000000

## IMPORTANT
Immediately upon launch, a database is considered to be in a “cold” state, as most if not all data is “frozen” in disk storage.
The database “working set” or “cache” — that is, the portion of data in active memory — is near empty, 
and all queries require reading from disk, which is one of the slowest functions of any DBMS. Queries executed shortly 
following a database restart are thus among the slowest to return their results.

As the DBMS responds to more queries, more data is read into active memory, and the database gradually shifts into a “warm” state. 
The more data is in the working set, the “warmer” the database, and the more quickly queries return.
https://community.openlinksw.com/t/controlling-the-database-working-set-in-openlink-virtuoso/1044



| Query    | Execution Time 1 | Execution Time 2 | Execution Time 3 | Execution Time 4 | Execution Time 5 | Execution Time 6 | Execution Time 7 | Execution Time 8 | Execution Time 9 | Execution Time 10 |
|----------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|------------------|-------------------|
| query_1  | 30303           | 16679           | 16720           | 16691           | 16656           | 16668           | 16674           | 16633           | 16637           | 16649            |
| query_2  | 6502            | 3913            | 3889            | 3897            | 3893            | 3890            | 3895            | 3892            | 3890            | 3890             |
| query_4  | 1409            | 1284            | 1252            | 1256            | 1249            | 1247            | 1247            | 1247            | 1246            | 1253             |
| query_5  | 9630            | 112             | 121             | 116             | 112             | 118             | 113             | 113             | 110             | 112              |
| query_6  | 2684            | 2041            | 2055            | 2045            | 2051            | 2051            | 2050            | 2046            | 2070            | 2052             |
| query_7  | 116             | 115             | 125             | 117             | 115             | 120             | 115             | 113             | 113             | 114              |
| query_8  | 9808            | 706             | 710             | 706             | 707             | 713             | 707             | 702             | 712             | 705              |
| query_9  | 13892           | 13840           | 13839           | 13871           | 13873           | 13800           | 13905           | 13828           | 13854           | 13842            |
| query_10 | 48127           | 13881           | 13832           | 13857           | 13833           | 13812           | 13768           | 13815           | 13800           | 13844            |
| query_11 | 12537           | 13881           | 13853           | 13971           | 13856           | 13813           | 13848           | 13815           | 13799           | 13876            |



