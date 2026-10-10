class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxLength = 0

        for n in seen:
            if (n-1) not in seen:
                currLength = 1
                while (n + currLength) in seen:
                    currLength += 1
                maxLength = max(maxLength, currLength)
        return maxLength
