class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, a in enumerate(nums):
            complement = target - a
            if complement in seen:
                return [seen[complement], i]
            seen[a] = i
        return [] 