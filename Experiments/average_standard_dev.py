import numpy as np

# Example data (1D array) — replace with your actual data
data = np.array([4473.9, 21283.8, 779.4, 26875.0, 2756.1, 1531.9, 3308.1, 2927.3, 756.2, 15890.7, 28598.8, 17944.2, 17981.5]



)
# Step 1–4: square, sum, divide by N, then sqrt
squared_sum = np.sum(data ** 2)
n = len(data)
result = np.sqrt(squared_sum / n)

#average = np.mean(data)
#print(f"Average of values: {average:.4f}")
print(f"Square root of average of squared values: {result:.4f}")