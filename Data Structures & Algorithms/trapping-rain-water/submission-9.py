class Solution:
    def trap(self, height: List[int]) -> int:
        '''
        two pointers
        1. initialize two pointers at the indices of both ends of the list
        2. initialize the left and right max with the heights at these indices(water can never be trapped here)
        3. to get the units of water trapped for every other index:
            - compute the min(maxL, maxR) - height[i]
            - the smaller value between the left max and the right max is the bottleneck
        4. return the total water trapped

        time: O(n)
        space: O(1)
        '''

        l, r = 0, len(height)-1
        maxL, maxR = height[l], height[r]
        total = 0

        while l < r:
            if maxL < maxR:
                l += 1
                maxL = max(maxL, height[l])
                total += maxL - height[l]
            else:
                r -= 1
                maxR = max(maxR, height[r])
                total += maxR - height[r]

        return total

