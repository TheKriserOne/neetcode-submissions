class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        def helper(index, slate):
            if index == len(nums):
                result.append(slate[:])
                return
            
            # Include
            slate.append(nums[index])
            helper(index + 1, slate)
            slate.pop()
            
            # handle duplicates
            while index + 1  < len(nums) and nums[index] == nums[index + 1]:
                index += 1

            # exclude
            helper(index + 1, slate)
            



        nums.sort()
        result = []
        helper(0, [])
        return result
        