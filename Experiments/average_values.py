import numpy as np
import pandas as pd

# Raw data string (replace this with reading from file if needed)
data_string = """
4935.9 
34516.8 
288.0
"""

# Convert string to list of lists (each sublist is a row)
data_lines = [list(map(float, line.strip().split(','))) for line in data_string.strip().split('\n')]

# Convert to NumPy array for processing
data_array = np.array(data_lines)  # shape: (10, 43)
print(f"Data shape: {data_array.shape}")
# Calculate average for each column (query)
averages = np.mean(data_array, axis=0)
std_devs = np.std(data_array, axis=0)

# Create DataFrame with results
query_ids = [f"query_{i+1}" for i in range(data_array.shape[1])]
df = pd.DataFrame({
    'category': query_ids,
    'average_time': averages,
    'std_dev': std_devs
})


# Output the table
print(df.to_string(index=False))
