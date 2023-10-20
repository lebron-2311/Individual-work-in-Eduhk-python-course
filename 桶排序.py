# writer：LeBron James
# My email 1269497440@qq.com
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


if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    print(bucket_sort(lst))
