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


# merge sort
def merge(self, low, mid, high):
    i = low
    j = mid + 1
    tmp = []
    while i <= mid and j <= high:
        if self[i] <= self[j]:
            tmp.append(self[i])
            i += 1
        else:
            tmp.append(self[j])
            j += 1
    while i <= mid:
        tmp.append(self[i])
        i += 1
    while j <= high:
        tmp.append(self[j])
        j += 1
    self[low:high + 1] = tmp


def mergesort(self, low, high):
    if low < high:
        mid = (low + high) // 2
        mergesort(self, low, mid)
        mergesort(self, mid + 1, high)
        merge(self, low, mid, high)


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
    sorted_array = None  # Initialize sorted_array variable

    if algorithm == "sorted":
        sorted_array = sorted(array)
    elif algorithm == "bubble":
        bubble(array)
        sorted_array = array
    elif algorithm == "mergesort":
        mergesort(array, 0, len(array) - 1)
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

selected_algorithms = ["sorted", "bubble", "mergesort", "bucket"]

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
