x = []       # Time (s)
mem = []     # %mem
cpu = []     # %cpu

with open('/home/eltaj-amirli/Desktop/Knowledge-Graph-Partitioning/Experiments/Experiment 1 HPC/monitor.log', 'r') as file:
    next(file)  # Skip the header line
    for line in file:
        parts = line.strip().split()
        if len(parts) < 4:
            continue  # Skip invalid/malformed lines
        x.append(int(parts[0]))      # First column (time) as integer
        mem.append(float(parts[1]))  # Third column (%mem) as float
        cpu.append(float(parts[2]))  # Fourth column (%cpu) as float

# Result:
# x = [60, 120, 180, 241, 301, ..., 24688]
# mem = [1.0, 1.2, 1.3, ..., 1.7]
# cpu = [35.7, 46.2, 53.1, ..., 85.8]