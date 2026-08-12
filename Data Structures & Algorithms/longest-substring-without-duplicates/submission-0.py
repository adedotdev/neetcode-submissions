class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0
        seen = {}

        slow, fast = -1, 0
        for c in s:
            if c not in seen or seen[c] < slow:
                seen[c] = fast
            else:
                slow = seen[c]
                seen[c] = fast
            res = max(res, fast-slow)
            fast += 1
        return res