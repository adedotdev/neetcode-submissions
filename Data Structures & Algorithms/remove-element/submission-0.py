class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        l, r = -1, 0
        while r < len(nums):
            if nums[r] != val:
                nums[l+1] = nums[r]
                l += 1
                k += 1
            r += 1
        return k