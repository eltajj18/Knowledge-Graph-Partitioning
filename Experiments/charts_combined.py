import matplotlib.pyplot as plt

# Initialize lists for both datasets
time_openml, memory_openml, cpu_openml = [], [], []
time_pwc, memory_pwc, cpu_pwc = [], [], []

# Read PwC data
with open('/home/eltaj-amirli/Desktop/Knowledge-Graph-Partitioning/Experiments/Experiment 2/monitor_log_files/monitor_pwc.log', 'r') as file:
    next(file)
    for line in file:
        parts = line.strip().split()
        if len(parts) < 4:
            continue
        time_pwc.append(int(parts[0]))
        memory_pwc.append(float(parts[2]))
        cpu_pwc.append(float(parts[3]))

# Read OpenML data
with open('/home/eltaj-amirli/Desktop/Knowledge-Graph-Partitioning/Experiments/Experiment 2/monitor_log_files/monitor_openml.log', 'r') as file:
    next(file)
    for line in file:
        parts = line.strip().split()
        if len(parts) < 4:
            continue
        time_openml.append(int(parts[0]))
        memory_openml.append(float(parts[2]))
        cpu_openml.append(float(parts[3]))

# Create subplots
fig, axs = plt.subplots(2, 1, figsize=(12, 8), sharex=True)

# Memory subplot
axs[0].plot(time_pwc, memory_pwc, marker='o', label='PwC', color='tab:blue')
axs[0].plot(time_openml, memory_openml, marker='x', label='OpenML', color='tab:green')
axs[0].set_ylabel('Memory Usage (%)')
axs[0].set_title('Memory Usage Over Time')
axs[0].legend()
axs[0].grid(True, which='both', linestyle='--', linewidth=0.5)

# CPU subplot
axs[1].plot(time_pwc, cpu_pwc, marker='o', label='PwC', color='tab:orange')
axs[1].plot(time_openml, cpu_openml, marker='x', label='OpenML', color='tab:red')
axs[1].set_xlabel('Time (s)')
axs[1].set_ylabel('CPU Usage (%)')
axs[1].set_title('CPU Usage Over Time')
axs[1].legend()
axs[1].grid(True, which='both', linestyle='--', linewidth=0.5)

plt.tight_layout()

# Save plot
plt.savefig("/home/eltaj-amirli/Desktop/Knowledge-Graph-Partitioning/Experiments/output_plot_experiment2.png")
plt.close()
