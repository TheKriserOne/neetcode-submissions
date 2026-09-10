class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1
        if nums[l] <= nums[r]:
            return nums[l]
        while nums[l] > nums[r] or nums[l] > nums[l - 1]:
            l = l + 1
            r = r - 1
        return nums[l] 
        