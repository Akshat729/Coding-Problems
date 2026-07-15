class Solution:
    def gcd(a, b):
        while b:
            a, b = b, a%b
        return a

    def gcdOfOddEvenSums(self, n: int) -> int:
        sumOdd = 0
        sumEven = 0

        for i in range(1, n*2+1):
            if i%2==0:
                sumEven += i
            else:
                sumOdd += i
        return gcd(sumOdd, sumEven)
        