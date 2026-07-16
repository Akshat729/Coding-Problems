class Solution:
    def gcd(a, b):
        return a if b==0 else gcd(b, a%b)

    def gcdSum(self, nums: list[int]) -> int:
        prefixGcd = []
        mxi = 0

        for i in nums:
            mxi = max(i, mxi)
            prefixGcd.append(gcd(i, mxi))

        prefixGcd.sort()
        i = 0
        j = len(prefixGcd) - 1
        total_sum = 0

        while i<j:
            total_sum += gcd(prefixGcd[i], prefixGcd[j])
            i += 1
            j -= 1
        return total_sum

        