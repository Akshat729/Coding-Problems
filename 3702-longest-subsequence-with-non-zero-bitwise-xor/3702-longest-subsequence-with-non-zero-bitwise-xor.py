class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        total = 0
        non_zero = False
        n = len(nums)

        for i in nums:
            non_zero = non_zero | i > 0
            total ^= i

        if total != 0:
            return n

        if non_zero:
            return n - 1

        return 0