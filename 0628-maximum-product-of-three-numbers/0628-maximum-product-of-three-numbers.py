class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums = sorted(nums)
        n = len(nums)
        first_max = nums[n-1]
        sec_max =  nums[n-2]
        third_max = nums[n-3]
        first_min = nums[0]
        sec_min = nums[1]

        prod1 = first_max * sec_max * third_max
        prod2 = first_min * sec_min * first_max
        
        if prod1 > prod2:
            return prod1
        return prod2
        