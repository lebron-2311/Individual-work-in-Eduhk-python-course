# writer：LeBron James
# My email 1269497440@qq.com
import time
import random


def bubble(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

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


def bucket_sort(arr):
    # 确定输入数组的最大值和最小值
    min_val = min(arr)
    max_val = max(arr)

    # 计算桶的数量
    num_buckets = max_val - min_val + 1

    # 创建空桶列表
    buckets = [[] for _ in range(num_buckets)]

    # 将元素分配到桶中
    for num in arr:
        index = num - min_val  # 计算元素应该放置在哪个桶中
        buckets[index].append(num)

    # 对每个桶中的元素应用其他排序算法（这里使用内置的排序函数）
    for i in range(num_buckets):
        buckets[i].sort()

    # 合并排序后的桶中的元素
    sorted_arr = [num for bucket in buckets for num in bucket]

    return sorted_arr


def run_sorting_algorithm(algorithm, array):
    """
    运行给定的排序算法并返回排序后的数组和执行时间。

    参数：
    algorithm（str）：排序算法的名称。
    array（list）：待排序的数组。

    返回：
    sorted_array（list）：排序后的数组。
    execution_time（float）：排序算法的执行时间。
    """
    start_time = time.time()

    if algorithm == "sorted":
        sorted_array = sorted(array)
    elif algorithm == "bubble":
        bubble(array)
    elif algorithm == "quicksort":
        quicksort(array, 0, len(array) - 1)
    elif algorithm == "bucket":
        bucket_sort(array)
    else:
        print("不支持的排序算法！")
        return None, None

    end_time = time.time()
    execution_time = end_time - start_time

    return sorted_array, execution_time


# 测试驱动程序
MIN_SIZE = 100000
MAX_SIZE = 5000000
INTERVAL = 50000

selected_algorithms = ["sorted", "bubble", "quicksort", "bucket"]

for size in range(MIN_SIZE, MAX_SIZE + 1, INTERVAL):
    # 生成随机数组
    array = [random.randint(1000000000, 9999999999) for _ in range(size)]

    for algorithm in selected_algorithms:
        sorted_array, execution_time = run_sorting_algorithm(algorithm, array)
        print(f"数据集大小：{size}，排序算法：{algorithm}，执行时间：{execution_time}秒")
