# Definition for singly-linked list.
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

    def countPrimeSetBits(self, left: int, right: int) -> int:
        ans = 0
        for i in range(left, right + 1, 1):
            oneCount = one_bit_count(i)
            if is_prime(oneCount):
                ans += 1
        return ans


def one_bit_count(n) -> int:
    ans = 0
    i = 0
    while i < 32:
        if n & (1 << i) != 0:
            ans += 1
        i += 1
    return ans


def is_prime(n) -> bool:
    sqrt = int(math.sqrt(n))
    for i in range(2, sqrt + 1, 1):
        if n % i == 0:
            return False
    return True


if __name__ == "__main__":
    s = Solution()
    print(s.countPrimeSetBits(6, 10))