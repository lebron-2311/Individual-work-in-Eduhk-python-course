# writer：LeBron James
# My email 1269497440@qq.com
# 11517840 Bowen Zheng
import time


# Transposition sorting
def bubblesort():
    list = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    for i in range(len(list)):  # 比较i 和 i+1 所以从0到len(list)-1
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]  # 交换两个数的位置
    print(list)


bubblesort()
print("*" * 90)
print(bubblesort())
print("*" * 90)
"""代码打印None是因为你在print(bubblesort())中调用了bubblesort()函数，而该函数没有返回任何值。
   在Python中，如果函数没有显式使用return语句返回一个值，那么默认情况下它会返回None。
   为了解决这个问题，你可以直接调用bubblesort()函数而不需要将其作为参数传递给print()函数"""


# 时间复杂度
def evaluate_time():
    start_time = time.time()
    bubblesort()
    end_time = time.time()
    print("Execution time:", end_time - start_time)


evaluate_time()

print("*" * 90)
import random


def generate_random_list(length):
    random_list = [random.randint(1, 1000) for _ in range(length)]
    return random_list


# Example usage
random_list = generate_random_list(100)
print(random_list)
