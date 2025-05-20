import matplotlib.pyplot as plt

# Sample data from earlier

time = []       # Time (s)
memory = []     # %mem
cpu = []     # %cpu

with open('/home/eltaj-amirli/Desktop/Knowledge-Graph-Partitioning/Experiments/Experiment 1 HPC/monitor.log', 'r') as file:
    next(file)  # Skip the header line
    for line in file:
        parts = line.strip().split()
        if len(parts) < 4:
            continue  # Skip invalid/malformed lines
        time.append(int(parts[0]))      # First column (time) as integer
        memory.append(float(parts[2]))  # Third column (%mem) as float
        cpu.append(float(parts[3]))  # Fourth column (%cpu) as float


# Create subplots
fig, axs = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# Memory subplot
axs[0].plot(time, memory, marker='o', color='tab:blue')
axs[0].set_ylabel('Memory Usage (%)')
axs[0].set_title('Memory Usage Over Time')
axs[0].grid(True, which='both', linestyle='--', linewidth=0.5)

# CPU subplot
axs[1].plot(time, cpu, marker='o', color='tab:orange')
axs[1].set_xlabel('Time (s)')
axs[1].set_ylabel('CPU Usage (%)')
axs[1].set_title('CPU Usage Over Time')
axs[1].grid(True, which='both', linestyle='--', linewidth=0.5)

plt.tight_layout()
# Set y-axis to show individual increments
plt.yticks(range(0, 101, 5))  # Showing from 0 to 100 in steps of 1

# Save plot
output_path = "/home/eltaj-amirli/Desktop/Knowledge-Graph-Partitioning/Experiments/output_plot.png"
plt.savefig(output_path)
plt.close()
