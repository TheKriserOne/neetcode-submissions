class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        possible_combinations = 2 ** len(nums)
        combinations = []

        for i in range(0, possible_combinations ):
            bits = list(map(int, bin(i)[2:].zfill(len(nums))))
            filtered = [value for i, value in enumerate(nums) if bits[i] == 1]
            combinations.append(filtered)
        return combinations

            
        

        