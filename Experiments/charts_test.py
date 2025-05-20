import os
import matplotlib.pyplot as plt
import pandas as pd

# Configuration
LOG_DIR = "/home/eltaj-amirli/Desktop/Knowledge-Graph-Partitioning/Experiments/Experiment 1 HPC/"  # Update this path
OUTPUT_DIR = "/home/eltaj-amirli/Desktop/Knowledge-Graph-Partitioning/Experiments/output_plot_test.png"  # Update this path

def process_log_file(file_path, output_dir):
    # Read log file
    df = pd.read_csv(file_path, delim_whitespace=True)
    
    # Convert KB to GB for memory size
    df['memory_gb'] = df['size (kb)'] / 1e6
    
    # Create figure with twin axes
    fig, ax1 = plt.subplots(figsize=(14, 7))
    
    # CPU Plot
    color = 'tab:red'
    ax1.set_xlabel('Time (seconds)')
    ax1.set_ylabel('CPU Usage (%)', color=color)
    ax1.plot(df['time'], df['%cpu'], color=color, marker='o', markersize=4, linestyle='-', linewidth=1)
    ax1.tick_params(axis='y', labelcolor=color)
    ax1.grid(True, linestyle='--', alpha=0.7)
    ax1.set_ylim(0, 100)  # CPU percentage range

    # Memory Plot (two different metrics)
    ax2 = ax1.twinx()
    color = 'tab:blue'
    
    # Plot both memory metrics
    ax2.set_ylabel('Memory (GB & %)', color=color)
    ax2.plot(df['time'], df['memory_gb'], color=color, marker='s', markersize=4, linestyle='--', linewidth=1, label='Memory Size (GB)')
    ax2.plot(df['time'], df['%mem'], color='tab:green', marker='^', markersize=4, linestyle='-.', linewidth=1, label='Memory Usage (%)')
    ax2.tick_params(axis='y', labelcolor=color)
    
    # Set appropriate limits
    ax2.set_ylim(
        bottom=min(df['memory_gb'].min(), df['%mem'].min()) * 0.9,
        top=max(df['memory_gb'].max(), df['%mem'].max()) * 1.1
    )

    # Title and legend
    base_name = os.path.basename(file_path)
    plt.title(f'System Metrics - {base_name}')
    fig.tight_layout()
    
    # Combine legends from both axes
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left')

    # Save plot
    output_path = os.path.join(output_dir, f"metrics_{os.path.splitext(base_name)[0]}.png")
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()

# Process all log files
for log_file in os.listdir(LOG_DIR):
    if log_file.endswith(".log"):
        full_path = os.path.join(LOG_DIR, log_file)
        process_log_file(full_path, OUTPUT_DIR)

print(f"Plots saved to: {OUTPUT_DIR}")