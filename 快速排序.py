# writer：LeBron James
# My email 1269497440@qq.com
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

if __name__ == '__main__':
    lst = [1, 3, 5, 7, 9, 2, 4, 6, 8, 0]
    quicksort(lst, 0, len(lst) - 1)
    print(lst)