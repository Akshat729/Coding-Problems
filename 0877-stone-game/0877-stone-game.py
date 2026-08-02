class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        dp_array = list(piles)

        for i in range(n-2, -1, -1):
            for j in range(i+1, n):
                dp_array[j] = max(piles[i] - dp_array[j], piles[j] - dp_array[j-1])
        return dp_array[-1] >= 0
        