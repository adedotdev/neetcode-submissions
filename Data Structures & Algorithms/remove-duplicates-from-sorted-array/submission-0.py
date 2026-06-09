class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 1
        l, r = 0, 1
        while(r < len(nums)):
            if nums[r] != nums[l]:
                nums[l+1] = nums[r]
                l += 1
                k += 1
            r += 1
        return k