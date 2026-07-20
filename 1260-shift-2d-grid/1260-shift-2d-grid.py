class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        total = m*n
        k = k%total

        arr_1d = [i for j in grid for i in j] 
        arr_1d = arr_1d[total-k:] + arr_1d[:total-k]
   
        grid = [arr_1d[i:i + n] for i in range(0, len(arr_1d), n)]

        return grid

        