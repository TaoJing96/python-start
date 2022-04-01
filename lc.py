# Definition for singly-linked list.
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
    def levelOrder(self, root: TreeNode) -> List[int]:
        nodes = [root]
        ans = []
        while len(nodes) > 0:
            tmp = []
            for node in nodes:
                ans.append(node.val)
                if node.left is not None:
                    tmp.append(node.left)
                if node.right is not None:
                    tmp.append(node.right)
            nodes = tmp
        return nodes

# [6,3] [7, 5]
if __name__ == "__main__":
    s = Solution()
    print(s.hasAlternatingBits(7))