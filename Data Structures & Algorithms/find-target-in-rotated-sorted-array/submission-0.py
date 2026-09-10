class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        pos = 0
        length = r      
        while l <= r:
            if nums[l] <= nums[r]:
                if nums[l] < nums[pos]:
                    pos = l
                break

            mid = (l + r) // 2

            if nums[mid] < nums[pos]:
                pos = mid

            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        r = length
        l = 0
        while l <= r:
            mid = (l + r) // 2
            adjusted_mid = (mid + pos) % (length + 1)
            if target > nums[adjusted_mid]:
                l = mid + 1
            elif target < nums[adjusted_mid]:
                r = mid - 1
            else:
                return adjusted_mid
        return -1




        

        