class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        minimum = nums[0]
        while l <= r:
            if nums[l] < nums[r]:
                minimum = min(nums[l], minimum)
                return minimum
            mid = (l + r) // 2
            minimum = min(nums[mid], minimum)
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1

        return minimum
