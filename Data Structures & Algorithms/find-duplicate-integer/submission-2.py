class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        '''
        two pointers
        1. treat each index as the node and the value as a pointer to the next node
        2. using Floyd's Algorithm, find the beginning of the linked list cycle


        proof:
        slow = p + c - x
        fast = p + 2c - x

        if 2 * slow = fast,
        then:

        2 * (p + c - x) = p + 2c - x
        2p + 2c - 2x = p + 2c - x
        2p - 2x = p - x
        p - x = 0
        p = x

        where p is the distance between the head of the linked list and the start of the cycle,
        and x is the distance between the first intersection of the two pointers and the start of the cycle

        time: O(n)
        space: O(1)
        '''

        slow, fast = nums[0], nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        slow2 = nums[0]
        while slow != slow2:
            slow = nums[slow]
            slow2 = nums[slow2]
        
        return slow