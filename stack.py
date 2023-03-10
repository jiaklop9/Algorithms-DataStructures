#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""栈: 后进先出
"""


class Stack(object):
    def __init__(self):
        self.list = list()

    def push(self, item):
        self.list.append(item)

    def pop(self):
        self.list.pop()

    def peek(self):
        """返回栈顶元素"""
        return self.list[-1] if self.list else None

    def is_empty(self):
        return True if not len(self.list) else False

    def length(self):
        return len(self.list)
