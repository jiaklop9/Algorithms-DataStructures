#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""单链表"""


class Node(object):
    def __init__(self, ele):
        self.element = ele
        self.next = None


class SingleNode(object):
    def __init__(self, node=None):
        # 元素
        self.head = node

    def is_empty(self):
        return True if self.head is None else False

    def _length(self):
        cursor = self.head
        cnt = 0
        while cursor.next is not None:
            cnt += 1
            cursor = cursor.next
        return cnt

    def travel(self):
        """遍历"""
        cursor = self.head
        while cursor is not None:
            print(cursor.element)
            cursor = cursor.next

    def add(self, item):
        node = Node(item)
        node.next = self.head
        self.head = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
        else:
            cursor = self.head
            while cursor.next is not None:
                cursor = cursor.next
            cursor.next = node

    def remove(self, item):
        cursor = self.head
        pre = None
        while cursor is not None:
            if cursor.element == item:
                # 判断是否是头节点
                if cursor == self.head:
                    return
                else:
                    # 尾部节点及其他情况
                    pre.next = cursor.next
                return
            else:
                pre = cursor
                cursor = cursor.next

    def insert(self, position, index):
        node = Node(index)
        if position <= 0:
            self.add(index)
        elif position >= self._length() - 1:
            self.append(index)
        else:
            pre = self.head
            cnt = 0
            while cnt < position - 1:
                cnt += 1
                pre = pre.next
            node.next = pre.next
            pre.next = node

    def search(self, item):
        cursor = self.head
        while cursor is not None:
            if cursor.element == item:
                return True
            else:
                cursor = cursor.next
        return False


if __name__ == '__main__':
    ll = SingleNode()
    print(ll.is_empty())
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.add(10)
    ll.insert(-1, 9)
    ll.insert(2, 11)
    ll.travel()
    # 9， 10，11， 1，2，3
    # ll.search(11)
    ll.remove(11)
    ll.travel()
    print(ll.is_empty())
