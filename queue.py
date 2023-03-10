#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""队列：一端插入，一端弹出"""


class Queue(object):
    def __init__(self):
        self.list = list()

    def enqueue(self, item):
        """具体看那种常用那种操作，若经常添加，则添加端在队尾"""
        self.list.append(item)

    def dequeue(self):
        self.list.pop()

    def peek(self):
        """返回栈顶元素"""
        return self.list[-1] if self.list else None

    def is_empty(self):
        return True if not len(self.list) else False

    def length(self):
        return len(self.list)