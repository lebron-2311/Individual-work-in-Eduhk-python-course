# writer：LeBron James
# My email 1269497440@qq.com
import time
import random


# Bubble Sort
def bubble(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


# Quicksort
def partition(arr, left, right):
    pivot = arr[right]
    i = left - 1
    for j in range(left, right):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[right] = arr[right], arr[i + 1]
    return i + 1


def quicksort(arr, left, right):
    if left < right:
        q = partition(arr, left, right)
        quicksort(arr, left, q - 1)
        quicksort(arr, q + 1, right)


# Bucket Sort
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

    if algorithm == "sorted":
        sorted_array = sorted(array)
    elif algorithm == "bubble":
        bubble(array)
        sorted_array = array
    elif algorithm == "quicksort":
        quicksort(array, 0, len(array) - 1)
        sorted_array = array
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

selected_algorithms = ["sorted", "bubble", "quicksort", "bucket"]

# Dictionary to store execution times for each algorithm and dataset size
execution_times = {algorithm: [] for algorithm in selected_algorithms}

for size in range(MIN_SIZE, MAX_SIZE + 1, INTERVAL):
    array = [random.randint(1000000000, 9999999999) for _ in range(size)]

    for algorithm in selected_algorithms:
        _, execution_time = run_sorting_algorithm(algorithm, array)
        execution_times[algorithm].append(execution_time)
        print(f"数据集大小：{size}，排序算法：{algorithm}，执行时间：{execution_time}秒")

# Generate graphics or tables using the execution_times data structure and analyze the outcomes based on Big-O notation

# Write your report including background information, analysis process, findings, and conclusions.
