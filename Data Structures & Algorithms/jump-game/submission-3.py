class Solution:
    def canJump(self, nums: List[int]) -> bool:
        maxReach = 0
        for i, a in enumerate(nums): 
            if i > maxReach:
                return False
            maxReach = max(maxReach, i + a)
        return True
