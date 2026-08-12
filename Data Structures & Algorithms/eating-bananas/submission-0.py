class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        '''
        binary search
        1. initialize two pointers with the min and max number of piles in the array
        2. declare a variable to keep track of the min-eating-rate
        3. perform a binary search on the two ends of the array using the pointers
            - compare the middle number gotten from the binary search against each pile to
              see if all piles can be consumed within the max number of hours given
            - if the total num of hours exceeds h, move the left pointer
            - if the total num of hours is less that h, update the min-eating-rate and move the right 
              pointer
        '''

        left, right = 1, max(piles)
        res = max(piles)
        while left <= right:
            k = (left + right) // 2
            num_of_hours = 0
            for p in piles:
                num_of_hours += math.ceil(p/k)

            if num_of_hours > h:
                left = k + 1
            elif num_of_hours <= h:
                res = k
                right = k - 1

        return res