class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        need to compute the max amount of money that can be taken at each step

        # recursion
        def helper(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            return max(helper(i-1), nums[i] + helper(i-2))
        return helper(len(nums)-1)
        '''

        # memoization
        memo = {}
        def helper(i):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])
            if i in memo:
                return memo[i]
            memo[i] = max(helper(i-1), nums[i] + helper(i-2))
            return memo[i]
        return helper(len(nums)-1)