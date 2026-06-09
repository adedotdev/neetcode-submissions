class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1Map = Counter(s1)

        l, r = 0, len(s1)
        while r <= len(s2):
            s2Map = Counter(s2[l:r])
            if s1Map == s2Map:
                return True
            l += 1
            r += 1
        return False