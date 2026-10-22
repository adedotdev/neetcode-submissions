class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        - start with brute force to understand the problem
        - the approach requires that you iterate over a potential solution set 
          starting at a k-eating-speed of 1 all the way to the max pile in the input array (i.e [1...4])
        - time: O(max(n) * n), where n is the size of the input array
        - optimize by performing binary search on this solution set

        binary search
        1. initialize two pointers with the min and max number of piles in the array
        2. declare a variable to keep track of the min-eating-rate
        3. perform a binary search on the two ends of the array using the pointers
            - compare the middle number gotten from the binary search against each pile to
              see if all piles can be consumed within the max number of hours given
            - if the total num of hours exceeds h, move the left pointer
            - if the total num of hours is less that h, update the min-eating-rate and move the right 
              pointer
    
        time: O(log(max(n)) * n)
        space: 
        '''

        l, r = 1, max(piles)
        res = max(piles)
        while l <= r:
            k = (l + r) // 2
            currHours = 0
            for p in piles:
                currHours += math.ceil(p/k)

            if currHours <= h:
                res = min(res, k)
                r = k - 1
            else:
                l = k + 1
        return res