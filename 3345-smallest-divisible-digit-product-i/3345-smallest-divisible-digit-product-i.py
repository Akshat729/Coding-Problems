class Solution:
    def mult(self, n):
        res = 1
        arr = str(n)
        for i in arr:
            res = res * int(i)
        return res

    def smallestNumber(self, n: int, t: int) -> int:
        for i in range(n, 101):
            res = self.mult(i)
            if res % t == 0:
                return i
        return t