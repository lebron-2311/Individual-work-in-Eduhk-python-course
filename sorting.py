ARRAY_LENGTH = 10000
from random import randint


def bubblesort():
    list = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    for i in range(len(list)):  # 比较i 和 i+1 所以从0到len(list)-1
        for j in range(len(list) - i - 1):
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]  # 交换两个数的位置
    print(list)


def run_sorting_algorithm(algorithm, array):
    # Build our array
    if algorithm == "sorted":
        sorted_array = sorted(array)
        print("排序后的数组:", sorted_array)
    elif algorithm == "bubblesort":
        bubblesort()
    else:
        print("算法名称错误")


if __name__ == "__main__":
    # Generate an array of `ARRAY_LENGTH` items consisting
    # of random integer values between 0 and 999
    array = [randint(0, 1000) for i in range(ARRAY_LENGTH)]

    # Call the function using the name of the sorting algorithm
    # and the array you just created
    run_sorting_algorithm(algorithm="sorted", array=array)
