#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def binary_search(data, item):
    """二分查找：前提有序队列
    递归实现
    """
    _len = len(data)
    if not _len:
        return False
    mid = _len // 2
    if data[mid] == item:
        return True
    if data[mid] > item:
        return binary_search(data[:mid], item)
    else:
        return binary_search(data[mid + 1:], item)


def binary_search_2(data, item):
    """非递归实现"""
    first = 0
    last = len(data) - 1
    while first <= last:
        mid = (first + last) // 2  # 取整
        if data[mid] == item:
            return True
        elif data[mid] > item:
            last = mid - 1
        else:
            first = mid + 1
    return False


if __name__ == '__main__':
    alist = [1, 2, 3, 33, 44, 55]
    print(alist)
    print(binary_search(alist, 33))
    print(binary_search_2(alist, 33))
