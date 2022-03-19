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

    result = 0

    def movingCount(self, m: int, n: int, k: int) -> int:
        self.result = 0
        trace = [[False for i in range(n)] for i in range(m)]
        self.dfs(m, n, k, 0, 0, trace)
        return self.result

    def dfs(self, m: int, n: int, k: int, x: int, y: int, trace: List[List[bool]]):
        if x >= m or x < 0 or y >= n or y < 0 or not trace[x][y]:
            return
        if self.bitSum(x) + self.bitSum(y) > k:
            return
        self.result += 1
        trace[x][y] = True
        self.dfs(m, n, k, x - 1, y, trace)
        self.dfs(m, n, k, x + 1, y, trace)
        self.dfs(m, n, k, x, y - 1, trace)
        self.dfs(m, n, k, x, y + 1, trace)

    def bitSum(self, m: int) -> int:
        ans = 0
        while m > 0:
            ans += m % 10
            m //= 10
        return ans


if __name__ == "__main__":
    s = Solution()

    print(1 + "" + 2)