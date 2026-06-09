class Solution:
    def maxArea(self, heights: List[int]) -> int:
        '''
        two pointers
        1. initialize two variables left and right at both ends of the list (0, len(height)-1)
        2. declare a variable maxArea to track the maximum area of the container
        3. iterate through array
            - calculate the area with each iteration and compute the max calculated so far
            - with each iteration, alternate decrementing the left and right and right until they converge (l < r)
        4. return maxArea
        '''

        maxArea = 0
        l, r = 0, len(heights)-1

        while l < r:
            currArea = min(heights[l], heights[r]) * (r-l)
            maxArea = max(currArea, maxArea )
            if heights[l] <= heights[r]:
                l += 1
            else:
                r -= 1
        return maxArea