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


class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        if not head:
            return head
        self.double(head)
        self.setRandom(head)
        return self.split(head)

    def double(self, head: 'Node'):
        while head:
            n = Node(head.val)
            n.next = head.next
            head.next = n
            head = n.next


    def setRandom(self, head: 'Node'):
        while head:
            if head.random:
                head.next.random = head.random.next
            head = head.next.next


    def split(self, head: 'Node') -> 'Node':
        ans = head.next
        while head:
            next = head.next
            head.next = next.next
            if next.next:
                next.next = next.next.next
            head = head.next
        return ans

if __name__ == "__main__":
    s = Solution()
    n1 = Node(1)
    n2 = Node(2)
    n3 = Node(3)
    n1.random = n3
    n1.next = n2
    n2.next = n3
    n = s.copyRandomList(n1)
    print(n)