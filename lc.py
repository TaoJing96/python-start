# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = dict()
        l, r = 0, 0
        ans = 1
        while r < len(s):
            if s[r] not in d or d[s[r]] < l:
                ans = max(ans, r - l + 1)
            else:
                v = d.get(s[r])
                ans = max(ans, r - l)
                l = v + 1
            d[s[r]] = r
            r += 1
        return ans


if __name__ == "__main__":
    solution = Solution()
    print(solution.lengthOfLongestSubstring("tmmzuxt"))
