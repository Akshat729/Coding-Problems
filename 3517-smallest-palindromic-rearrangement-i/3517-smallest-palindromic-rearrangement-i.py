class Solution:
    def smallestPalindrome(self, s: str) -> str:
        n = len(s)
        res = ''
        if n==1:
            return s

        if n%2==0:
            new_s = s[:n//2]
            new_s = ''.join(sorted(new_s))
            res = new_s + new_s[::-1]
        else:
            new_s = s[:(n//2)]
            middle = s[n//2]
            new_s = ''.join(sorted(new_s))
            res = new_s[:len(new_s)] + middle + new_s[::-1]

        return res
        
        