# Definition for singly-linked list.
import copy
import math
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# class Node:
#     def __init__(self, val=None, children=None):
#         self.val = val
#         self.children = children


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    preNode = None
    firstNode = None

    def treeToDoublyList(self, root: 'Node') -> 'Node':
        if root is None:
            return root
        self.preNode = None
        self.firstNode = None
        self.post_order(root)
        self.firstNode.left = self.preNode
        self.preNode.right = self.firstNode
        return self.firstNode


    def post_order(self, root: 'Node'):
        if root is None:
            return
        left = root.left
        right = root.right
        self.post_order(left)
        if not self.firstNode:
            self.firstNode = root
        if self.preNode:
            self.preNode.right = root
            root.left = self.preNode
        self.preNode = root
        self.post_order(right)


if __name__ == "__main__":
    s = Solution()
    n1 = Node(1)
    n = s.treeToDoublyList(n1)
    print(n)