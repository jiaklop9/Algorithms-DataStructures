#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Node(object):
    def __init__(self, item):
        self.item = item
        self.left = None
        self.right = None


class BinaryTree(object):
    def __init__(self):
        self.ls = list()
        self.root = None

    def add(self, item):
        node = Node(item)
        if self.root is None:
            self.root = node
            self.ls.append(self.root)
            print('add root: %s' % node.item)
        else:
            root = self.ls[0]
            if root.left is None:
                root.left = node
                self.ls.append(root.left)
                print('add root left: %s, %s' % (root.item, node.item))
            else:
                if root.right is None:
                    root.right = node
                    self.ls.append(root.right)
                    print('add root right: %s, %s' % (root.item, node.item))
                    self.ls.pop(0)

    @staticmethod
    def pre_order_stack(root):
        """
        前序遍历(根左右): 堆栈实现
        """
        if root is None:
            return
        stack = list()
        result = list()
        node = root
        while node or stack:
            while node:
                result.append(node.item)
                stack.append(node)
                # 不再有左子树，退出内循环
                node = node.left
            node = stack.pop()
            node = node.right
        print(result)

    def pre_order_stack_recursion(self, root):
        """
        前序遍历，递归实现
        """
        if root is None:
            return
        print('data: %s, left: %s, right: %s' % (root.item, root.left, root.right))
        self.pre_order_stack_recursion(root.left)
        self.pre_order_stack_recursion(root.right)


if __name__ == '__main__':
    tree = BinaryTree()
    for i in range(1, 11):
        tree.add(i)
    print('root: %s' % tree.root.item)
    # tree.pre_order_stack_recursion(tree.root)
    tree.pre_order_stack(tree.root)