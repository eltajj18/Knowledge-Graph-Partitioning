import matplotlib.pyplot as plt

# Sample data from earlier
time = [0, 60, 120, 180, 240, 300]
memory = [1.0, 1.1, 1.2, 1.3, 1.4, 1.5]
cpu = [34.5, 47.4, 55.8, 61.9, 66.6, 70.0]

# Plotting
plt.figure(figsize=(12, 6))
plt.plot(time, memory, marker='o', label='Memory Usage (%)')
plt.plot(time, cpu, marker='o', label='CPU Usage (%)')
plt.xlabel('Time (s)')
plt.ylabel('Usage (%)')
plt.title('Memory and CPU Usage Over Time')
plt.legend()
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Set y-axis to show individual increments
plt.yticks(range(0, 101, 5))  # Showing from 0 to 100 in steps of 1

# Save plot
output_path = "/home/eltaj-amirli/Desktop/Knowledge-Graph-Partitioning/Experiments/output_plot.png"
plt.savefig(output_path)
plt.close()

output_path
