# Query times in milliseconds
query_times = [
    133, 927, 2077, 3086, 18774, 82, 385, 1877, 141, 1727, 2087, 445986, 616766, 
    603074, 13792, 2203, 11367, 298, 296, 50500, 222, 444, 4044, 3858, 525, 
    832567, 14496, 21263, 1271, 325156, 14321, 2902, 4046, 412, 169841, 15241, 
    3332, 10545, 306, 147, 863, 993, 16, 19511, 5577, 2346, 11876, 4924, 156, 
    42613, 44112, 15721, 15731
]

# Query order
query_order = [
    1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 1, 2, 20, 21, 22, 23, 24, 25, 26, 
    27, 28, 29, 2, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 4, 40, 41, 42, 43, 44, 
    45, 46, 47, 48, 49, 50, 51, 52, 53, 6, 7, 8, 9
]

# Calculate cumulative sum
cumulative_sum = 0
threshold = 3345100 # 2,700,000 ms
for i, query_index in enumerate(query_order):
    cumulative_sum += query_times[query_index - 1]  # Subtract 1 for zero-based indexing
    if cumulative_sum >= threshold:
        print(f"Threshold reached at query {query_index} (position {i + 1} in the order).")
        print(f"Cumulative time: {cumulative_sum} ms")
        break