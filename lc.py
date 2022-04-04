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
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans = []
        queue = [root]
        flag = True
        while len(queue) > 0:
            temp = []
            level = []
            for node in queue:
                level.append(node.val)
                if node.left is not None:
                    temp.append(node.left)
                if node.right is not None:
                    temp.append(node.right)
            if not flag:
                queue.reverse()
            flag = not flag
            ans.append(level)
            queue = temp
        return ans

if __name__ == "__main__":
    s = Solution()
    print(s.hasAlternatingBits(7))