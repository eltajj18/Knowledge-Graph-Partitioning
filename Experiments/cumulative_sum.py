# Query times in milliseconds
query_times = [
2830,1285,2186,2614,10481,124,96,1781,314,770,1212,501074,790676,799548,18726,2687,8314,250,384,44961,111,595,1882,7566,548,934709,13884,24958,1656,361992,16736,2606,4914,381,211268,18764,4332,12418,600,142,858,933,16,10433,5630,1092,12014,3195,149,38679,49280,16563,16633
]

# Query order
query_order = [
    1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 24, 25, 26, 
    27, 28, 29, 3, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 4, 40, 41, 42, 43, 44, 
    45, 46, 47, 48, 49, 5, 50, 51, 52, 53, 6, 7, 8, 9
]

# Calculate cumulative sum
cumulative_sum = 0
threshold = 500733 # 2,700,000 ms
for i, query_index in enumerate(query_order):
    cumulative_sum += query_times[query_index - 1]  # Subtract 1 for zero-based indexing
    if cumulative_sum >= threshold:
        print(f"Threshold reached at query {query_index} (position {i + 1} in the order).")
        print(f"Cumulative time: {cumulative_sum} ms")
        break

