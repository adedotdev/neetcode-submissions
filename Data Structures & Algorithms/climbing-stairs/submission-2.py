class Solution:
    def climbStairs(self, n: int) -> int:
        prev = curr = 1
        for i in range(1, n):
            next = curr + prev
            prev = curr
            curr = next
        return curr