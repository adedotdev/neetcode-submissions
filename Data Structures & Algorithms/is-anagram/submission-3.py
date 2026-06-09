from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): return False
        
        seen = Counter(s)
        for n in t:
            if n in seen:
                if seen[n] == 0:
                    return False
                seen[n] -= 1;
            else:
                return False
        return True
        