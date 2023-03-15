#!/usr/bin/env python3
# -*- coding:utf-8 -*-


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
