#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def merge_sort(data):
    """归并排序思想：
        先递归分解数组，再合并数组.
        将数组分解后，比较两个数组最前边的数，谁小取谁，然后相应指针往后移动，直到一个数组为空，
        然后把另外一个数组剩下数据移动过来就行。
    """
    _len = len(data)
    if len(data) <= 1:
        return data
    mid = _len // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    left_cursor, right_cursor = 0, 0
    result = list()
    while left_cursor < len(left) and right_cursor < len(right):
        if left[left_cursor] < right[right_cursor]:
            result.append(left[left_cursor])
            left_cursor += 1
        else:
            result.append(right[right_cursor])
            right_cursor += 1
    result += left[left_cursor:]
    result += right[right_cursor:]
    return result


if __name__ == '__main__':
    alist = [4, 1, 2, 3, 12, 33, 44, 56]
    print(alist)
    print(merge_sort(alist))
