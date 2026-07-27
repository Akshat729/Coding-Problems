class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        prod = 0
        for i in range(n):
            for j in range(i+1, n):
                prod = max(((nums[i] - 1) * (nums[j] - 1)), prod)
        return prod
                
        