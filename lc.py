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


# 【3,4,5,1,2] 为 [1,2,3,4,5] 2 3 1  2
class Solution:
    def minArray(self, numbers: List[int]) -> int:
        l = 0
        r = len(numbers) - 1
        while l < r:
            mid = (l + r) >> 1
            if numbers[r] == numbers[l]:
                l += 1
            elif numbers[r] >= numbers[mid]:
                r = mid
            else:
                l = mid + 1
        return numbers[l]


if __name__ == "__main__":
    s = Solution()
    print(s.minArray([3, 4, 5, 1, 2]))
