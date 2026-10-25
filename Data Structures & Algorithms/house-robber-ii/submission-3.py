class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        if the first house is robbed, the last house is not allowed (0 to n-2) -> nums[:-1]
        if the first house is not robber, the last house is allowed (1 to n-1) -> nums[1:]
        '''
        if len(nums) == 1:
            return nums[0]
        return max(self.helper(nums[1:]), self.helper(nums[:-1]))


    def helper(self, nums):
        # dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        n = len(nums)
        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        dp = [0] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, n):
            dp[i] = max(dp[i-1], nums[i] + dp[i-2])
        return dp[n-1] 

        # res = 0
        # memo = {}
        # def dfs(i):
        #     if i == 0:
        #         return nums[0]
        #     if i == 1:
        #         return max(nums[0], nums[1])
        #     if i in memo:
        #         return memo[i]
        #     memo[i] = max(dfs(i - 1), nums[i] + dfs(i - 2))
        #     return memo[i]
        # res = dfs(len(nums)-1)
        # return res
       