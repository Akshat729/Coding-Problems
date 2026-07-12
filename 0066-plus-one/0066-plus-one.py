class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = ''
        ans = []
        
        for i in digits:
            num += str(i)
        number = int(num) + 1

        while number>0:
            i = number%10
            number = number//10
            ans.append(int(i))
        return ans[::-1]

        
        