# Query times in milliseconds
query_times = [
1886,1051,2076,2471,9498,112,93,1844,338,340,1252,414356,613128,646878,15299,1884,7400,223,209,42060,89,533,2147,6787,549,865488,12803,20972,1250,308289,14009,2838,4078,276,169602,16059,3523,11390,133,143,926,939,17,10089,5352,1038,9839,3287,148,32076,45987,15604,15682
]

# Query order
query_order = [
    1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 24, 25, 26, 
    27, 28, 29, 3, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 4, 40, 41, 42, 43, 44, 
    45, 46, 47, 48, 49, 5, 50, 51, 52, 53, 6, 7, 8, 9
]

# Calculate cumulative sum
cumulative_sum = 0
threshold = 2935044  # 2,700,000 ms
for i, query_index in enumerate(query_order):
    cumulative_sum += query_times[query_index - 1]  # Subtract 1 for zero-based indexing
    if cumulative_sum >= threshold:
        print(f"Threshold reached at query {query_index} (position {i + 1} in the order).")
        print(f"Cumulative time: {cumulative_sum} ms")
        break

