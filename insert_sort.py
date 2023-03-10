#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""选择排序：
选取第一个为基准创建有序队列，之后设定为无序队列，
取无序队列元素与之前有序队列比较，插入合适位置
"""


def insert_sort(data):
    _len = len(data)
    for i in range(1, _len):
        # [1,2,3,4, ..., n-1]
        j = i  # j代表内层循环起始值
        while j > 0:
            if data[j] < data[j - 1]:
                data[j], data[j - 1] = data[j - 1], data[j]
                j -= 1
            else:
                break
    print(data)


if __name__ == '__main__':
    insert_sort([1, 23, 44, 56, 123])
