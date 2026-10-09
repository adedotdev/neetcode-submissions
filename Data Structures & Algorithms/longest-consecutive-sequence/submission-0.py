class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxLength = 0

        for n in nums:
            if (n - 1) not in seen:
                currLength = 0
                while (n + currLength) in seen:
                    currLength += 1
                maxLength = max(currLength, maxLength)
        return maxLength