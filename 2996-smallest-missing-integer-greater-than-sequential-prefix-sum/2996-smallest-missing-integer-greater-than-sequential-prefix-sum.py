class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        n = len(nums)
        seen = set(nums)
        tot_sum = nums[0]

        for i in range(1, n):
            if nums[i] == nums[i - 1] + 1:
                tot_sum += nums[i]
            else:
                break
        while tot_sum in seen:
            tot_sum += 1
        
        return tot_sum


        