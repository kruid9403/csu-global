import random
import time
import tracemalloc

#Generate Test Data
def generate_test_data(num_items, max_weight, max_value, capacity):
    options = []

    # Loop over the item count to create weights and values
    for _ in range(num_items):
        weight = random.randint(1, max_weight)
        value = random.randint(1, max_value)
        options.append((weight,value))

    # Return the list of options and the entered capacity
    return options, capacity

def knapsack_recursive(options, capacity, current_index=0, memo=None):
    # Handle memoization
    if memo == None:
        memo = {}
    
    key = (current_index, capacity)
    
    if key in memo:
        return memo[key]
    # Stop recursion at when the index or capacity exceeds their max values
    if current_index >= len(options) or capacity <= 0:
        return 0
    
    weight, value = options[current_index]

    value_exclude = knapsack_recursive(options, capacity, current_index + 1)

    value_include = 0 
    if weight <= capacity:
        value_include = value + knapsack_recursive(options, capacity - weight, current_index + 1)
    
    # Get the greater of the values
    result = max(value_exclude, value_include)

    # Add the result to memoization for later use if necessary
    memo[key] = result

    return result

def get_max_value(options, capacity):
    # Set the return value
    max_value = 0
    # Set the range of the loops
    num_items = len(options)

    # Check the values and record the solution
    for i in range(1 << num_items):
        total_weight = 0
        total_value = 0

        for j in range(num_items):
            if (i >> j) & 1:
                weight, value = options[j]
                total_weight += weight
                total_value += value

        if total_weight <= capacity:
            max_value = max(max_value, total_value)
    
    return max_value

# Optimized 1D array solution
def space_optimized(options, capacity):
    #Create the solution array
    dp = [0] * (capacity + 1)
    for w,v in options:
        for weight in range(capacity, w - 1, -1):
            #Add the greater of the existing weight in dp or the new weight
            dp[weight] = max(dp[weight], dp[weight - w] + v)

    return dp[capacity]

for i in range(5):
    items = input("How many items: ")
    items_int = int(items)
    weight = input("Max weight: ")
    weight_int = int(weight)
    max_val = input("Max value: ")
    max_value = int(max_val)
    capacity = input("Capacity: ")
    cap = int(capacity)
    options, capacity = generate_test_data(items_int, weight_int, max_value, cap)

    tracemalloc.start()
    print(options)
    start = time.perf_counter()
    result_recursive = knapsack_recursive(options = options, capacity=capacity)
    print(f"trace recursive: {tracemalloc.get_traced_memory()}")
    elapsed_recursive = time.perf_counter() - start
    print("Knapsack recursive result: ", result_recursive)
    print(f"Recursive time: {elapsed_recursive:.6f} seconds")
    tracemalloc.stop()

    tracemalloc.start()
    start = time.perf_counter()
    result_brute = get_max_value(options, capacity)
    elapsed_brute = time.perf_counter() - start
    print(f"trace brute-force: {tracemalloc.get_traced_memory()}")
    print("Brute-force result: ", result_brute)
    print(f"Brute-force time: {elapsed_brute} seconds")
    tracemalloc.stop()

    tracemalloc.start()
    start = time.perf_counter()
    result_optimized = space_optimized(options, capacity)
    elapsed_optimized = time.perf_counter() - start
    print(f"trace optimized brute: {tracemalloc.get_traced_memory()}")
    print("Optimized result: ", result_optimized)
    print(f"Optimized time: {elapsed_optimized} seconds")
    tracemalloc.stop()