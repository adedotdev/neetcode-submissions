class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0
        last_index = len(nums)-1
        for index, battery in enumerate(nums): 
            if index > max_reachable:
                return False
            max_reachable = max(max_reachable, index + battery)
            if max_reachable >= last_index:
                return True