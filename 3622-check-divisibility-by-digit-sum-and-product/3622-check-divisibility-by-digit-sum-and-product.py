class Solution:
    def checkDivisibility(self, n: int) -> bool:
        val = str(n)
        sumOfnum = 0
        multOfnum = 1
        
        for i in val:
            sumOfnum += int(i)
            multOfnum *= int(i)

        if n % (multOfnum + sumOfnum) == 0:
            return True
        return False

        