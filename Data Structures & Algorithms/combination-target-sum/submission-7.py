class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(i, currSum, total):
            if i == len(nums) or total > target:
                return
            if total == target:
                res.append(currSum.copy())
                return
            
            currSum.append(nums[i])
            dfs(i, currSum, total + nums[i])

            currSum.pop()
            dfs(i+1, currSum, total)
        
        dfs(0, [], 0)
        return res