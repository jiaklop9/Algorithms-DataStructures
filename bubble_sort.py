#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""
冒泡排序： 每次选出最大或者最小数据，每次运行后，待比较数据长度减 1
"""


def bubble_sort(data):
    for num in range(len(data) - 1):
        for index in range(0, len(data) - 1 - num):
            if data[index] > data[index + 1]:
                data[index], data[index + 1] = data[index + 1], data[index]
    print(data)


def bubble_sort_1(data):
    for num in range(len(data) - 1):
        cnt = 0  # 是否有交换
        for index in range(0, len(data) - 1 - num):
            if data[index] > data[index + 1]:
                data[index], data[index + 1] = data[index + 1], data[index]
                cnt += 1
        if not cnt:
            break
    print(data)


if __name__ == '__main__':
    bubble_sort([1, 23, 12, 66, 31])
