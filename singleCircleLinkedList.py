#!/usr/bin/env python3
# -*- coding:utf-8 -*-


"""单向循环链表"""


class Node(object):
    def __init__(self, ele):
        self.element = ele
        self.next = None


class SingleCircleNode(object):
    def __init__(self, node=None):
        # 元素
        self.head = node
        # 构建循环
        if self.head:
            self.head.next = self.head

    def is_empty(self):
        return True if self.head is None else False

    def _length(self):
        if self.head is None:
            return 0
        cursor = self.head
        cnt = 1
        while cursor.next != self.head:
            cnt += 1
            cursor = cursor.next
        print('链表长度: %s' % cnt)
        return cnt

    def travel(self):
        """遍历"""
        if self.is_empty():
            return 
        cursor = self.head
        while cursor.next != self.head:
            print(cursor.element)
            cursor = cursor.next
        # 尾部节点未打印
        print(cursor.element)

    def add(self, item):
        node = Node(item)
        if self.head is None:
            self.head = node
            node.next = node
            return
        cursor = self.head
        while cursor.next != self.head:
            cursor = cursor.next
        # 退出时刚好是尾节点
        node.next = self.head
        self.head = node
        cursor.next = node

    def append(self, item):
        node = Node(item)
        if self.is_empty():
            self.head = node
            node.next = self.head
        else:
            cursor = self.head
            # 查询最后的节点
            while cursor.next != self.head:
                cursor = cursor.next
            cursor.next = node
            node.next = self.head

    def remove(self, item):
        if self.is_empty():
            return
        cursor = self.head
        pre = None
        while cursor.next != self.head:
            if cursor.element == item:
                # 判断是否是头节点
                if cursor == self.head:
                    # 头节点，找尾节点
                    rear = self.head
                    while rear.next != self.head:
                        rear = rear.next
                    self.head = cursor.next
                    rear.next = self.head
                else:
                    # 尾部节点及其他情况
                    pre.next = cursor.next
                break
            else:
                pre = cursor
                cursor = cursor.next
        if cursor.element == item:
            if cursor == self.head:
                self.head = None
            pre.next = cursor.next


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
        while cursor.next != self.head:
            if cursor.element == item:
                return True
            else:
                cursor = cursor.next
        if cursor.element == item:
            return True
        return False


if __name__ == '__main__':
    ll = SingleCircleNode()
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.travel()
    ll._length()
    ll.add(10)
    ll.travel()
    ll.remove(2)
    ll.travel()
    print(ll.is_empty())
