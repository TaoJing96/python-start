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
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        ans = []
        while left <= right:
            if self.legal(left):
                ans.append(left)
            left += 1
        return ans


    def legal(self, num: int) -> bool:
        n = num
        while n > 0:
            m = n % 10
            if m == 0 or num % m != 0:
                return False
            n //= 10
        return True


# [6,3] [7, 5]
if __name__ == "__main__":
    s = Solution()
    print(s.hasAlternatingBits(7))