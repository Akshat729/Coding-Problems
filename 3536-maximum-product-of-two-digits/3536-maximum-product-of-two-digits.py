class Solution:
    def getNumList(self, n):
        res = str(n)
        arr = []
        for i in res:
            arr.append(int(i))
        return sorted(arr)

    def maxProduct(self, n: int) -> int:
        arr = self.getNumList(n)
        s = len(arr)
        return arr[s-1] * arr[s-2]
        