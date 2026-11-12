class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        # recursion
        if n <= 1:
            return 1
        return self.climbStairs(n-1) + self.climbStairs(n-2)


        # top-down dp (memoization)
        memo = {}
        def helper(n):
            if n <= 1:
                return 1
            if n in memo:
                return memo[n]
            memo[n] = helper(n-1) + helper(n-2)
            return memo[n]
        return helper(n)
        # time: O(n)
        # space: O(n)


        # bottom-up dp (tabulation)
        prev = curr = 1
        for i in range(1, n):
            next = curr + prev
            prev = curr
            curr = next
        return curr
        # time: O(n)
        # space: O(1)
        '''

        memo = {}
        def helper(n):
            if n <= 1:
                return 1
            if n in memo:
                return memo[n]
            memo[n] = helper(n-1) + helper(n-2)
            return memo[n]
        return helper(n)