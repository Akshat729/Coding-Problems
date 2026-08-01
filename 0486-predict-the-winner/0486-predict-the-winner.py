class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)

        if n % 2 == 0:
            return True
        
        dp_array = list(nums)

        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                dp_array[j] = max(nums[i] - dp_array[j], nums[j] - dp_array[j-1])
        return dp_array[-1] >= 0

        