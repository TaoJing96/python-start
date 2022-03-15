# Definition for singly-linked list.
from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        return self.helper(preorder, inorder, 0, len(preorder) - 1, 0, len(inorder) - 1)

    def helper(self, preorder: List[int], inorder: List[int], preLeft: int, preRight: int, inLeft: int, inRight: int) -> Optional[TreeNode]:
        if preLeft > preRight or inLeft > inRight:
            return None
        for i in range(inLeft, inRight + 1):
            if inorder[i] == preorder[preLeft]:
                node = TreeNode(inorder[i])
                leftLen = i - inLeft
                node.left = self.helper(preorder, inorder, preLeft + 1, leftLen + preLeft, inLeft, i - 1)
                node.right = self.helper(preorder, inorder, leftLen + preLeft + 1, preRight, i + 1, inRight)
                return node
        return None


if __name__ == "__main__":
    solution = Solution()
