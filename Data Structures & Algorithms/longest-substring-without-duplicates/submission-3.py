class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
    #     s = -1, f = 0

    #     a b b a
    #       s   f

    #   res = (f-s) = 3

        seen = {}
        slow, fast = -1, 0
        res = 0
        for c in s:
            if c not in seen:
                seen[c] = fast
            else:
                if seen[c] < slow:
                    seen[c] = fast
                else:
                    slow = seen[c]
                    seen[c] = fast
            res = max(res, fast-slow)
            fast += 1
        return res
                