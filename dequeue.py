#!/usr/bin/env python3
# -*- coding:utf-8 -*-

"""双端队列：队列两端都可进行插入删除操作"""


class Dequeue(object):
    def __init__(self):
        self.list = list()

    def add_front(self, item):
        """头部添加"""
        self.list.insert(0, item)

    def add_end(self, item):
        self.list.append(item)

    def pop_front(self):
        self.list.pop(0)

    def pop_end(self):
        self.list.pop()

    def is_empty(self):
        return True if not self.list else False

    def size(self):
        return len(self.list)