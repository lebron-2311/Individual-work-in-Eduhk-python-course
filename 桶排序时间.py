# writer：LeBron James
# My email 1269497440@qq.com
import time
import random
def bucket_sort(arr):
    min_val = min(arr)
    max_val = max(arr)
    num_buckets = max_val - min_val + 1
    buckets = [[] for _ in range(num_buckets)]

    for num in arr:
        index = num - min_val
        buckets[index].append(num)

    for i in range(num_buckets):
        buckets[i].sort()

    sorted_arr = [num for bucket in buckets for num in bucket]
    return sorted_arr


# Run sorting algorithm and measure execution time
def run_sorting_algorithm(algorithm, array):
    start_time = time.time()
    sorted_array = None  # Initialize sorted_array variable

    if algorithm == "sorted":
        sorted_array = sorted(array)
    elif algorithm == "bucket":
        sorted_array = bucket_sort(array)
    else:
        print("不支持的排序算法！")
        return None, None

    end_time = time.time()
    execution_time = end_time - start_time

    return sorted_array, execution_time

# Test Driver Program
MIN_SIZE = 100000
MAX_SIZE = 5000000
INTERVAL = 50000

selected_algorithms = ["sorted", "bubble", "mergesort", "bucket"]

# Dictionary to store execution times for each algorithm and dataset size
execution_times = {algorithm: [] for algorithm in selected_algorithms}

for size in range(MIN_SIZE, MAX_SIZE + 1, INTERVAL):
    array = [random.randint(MIN_SIZE, MAX_SIZE) for _ in range(size)]


    for algorithm in selected_algorithms:
        _, execution_time = run_sorting_algorithm(algorithm, array)
        execution_times[algorithm].append(execution_time)
        print(f"数据集大小：{size}，排序算法：{algorithm}，执行时间：{execution_time}秒")