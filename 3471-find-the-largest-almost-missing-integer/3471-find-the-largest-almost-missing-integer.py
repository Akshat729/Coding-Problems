class Solution:
    def largestInteger(self, nums: List[int], k: int) -> int:
        freq = [0] * 51
        n = len(nums)
        res = -1

        for i in nums:
            freq[i] += 1
        if k==n:
            return max(nums)

        for i in range(n):
            if freq[nums[i]] == 1:
                if k == 1:
                    res = max(res, nums[i])
                elif (not i or i == n - 1):
                    res = max(res, nums[i])
        return res
        
        
        