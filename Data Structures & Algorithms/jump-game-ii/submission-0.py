class Solution:
    def jump(self, nums: List[int]) -> int:
        min_jumps = 0
        curr = 0
        maxReach = 0
        
        for i, a in enumerate(nums[:-1]):
            maxReach = max(maxReach, i + a)
            
            if i == curr:
                min_jumps += 1
                curr = maxReach
                
        return min_jumps