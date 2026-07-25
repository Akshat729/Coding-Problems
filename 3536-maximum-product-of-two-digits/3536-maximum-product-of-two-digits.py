class Solution:
    def getNumList(self, n):
        res = str(n)
        arr = []
        for i in res:
            arr.append(int(i))
        return sorted(arr)
    def maxProduct(self, n: int) -> int:
        arr = self.getNumList(n)
        prod = 0
        for i in range(1,len(arr)):
            if arr[i-1]*arr[i]>prod:
                prod = arr[i-1]*arr[i]
        return prod
        