#!/usr/bin/env python3
# -*- coding:utf-8 -*-


def select_sort(data):
    """选择出最小值下标，赋值，重复
    最外层: [0,1,2,3,4,...n-2, n-1]
    内层： 0，1，2，3 ...
    """
    for i in range(len(data)-1):
        _min = i
        for j in range(i + 1, len(data)):
            if data[_min] > data[j]:
                _min = j
        data[i], data[_min] = data[_min], data[i]
    print(data)


if __name__ == '__main__':
    select_sort([1, 23, 123, 45, 6, 77, 8, 22])
