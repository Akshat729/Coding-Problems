class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i,num in enumerate(nums):
            complement = target - num
            if complement in d:
                return [i, d[complement]]
            d[num] = i
        return []
