class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        res = []
        minNum = min(nums)
        maxNum = max(nums)

        for i in range(minNum, maxNum):
            if i not in nums:
                res.append(i)
                
        return res

        