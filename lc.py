# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        dp = [[0] * len(s) for _ in range(len(s))]
        maxLen = 1
        ans = s[0]
        for i in range(1, len(s)):
            for j in range(i - 1, -1, -1):
                if s[i] == s[j]:
                    if i - j <= 2:
                        dp[j][i] = i - j + 1
                    elif dp[j + 1][i - 1] > 0:
                        dp[j][i] = 2 + dp[j + 1][i - 1]
                if dp[j][i] > maxLen:
                    maxLen = dp[j][i]
                    ans = s[j:i+1]
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.longestPalindrome("aacabdkacaa"))
    print(solution.longestPalindrome("aacaa"))
    # print(solution.longestPalindrome("aca"))
