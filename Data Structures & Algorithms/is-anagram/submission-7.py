class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = Counter(s)

        for c in t:
            if c in seen:
                if seen[c] > 1:
                    seen[c] = seen.get(c) - 1
                else:
                    del seen[c]
            else:
                return False

        return True if len(seen) == 0 else False
