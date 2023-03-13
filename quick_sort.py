#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]
    for j in range(low, high):
        # 当前元素小于或等于 pivot
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    """
    :params: low:起始索引
    :params: high:结束索引
    """
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


if __name__ == '__main__':
    arr = [10, 7, 8, 9, 1, 5]
    n = len(arr)
    quick_sort(arr, 0, n - 1)
    print("排序后的数组: %s" % arr)
