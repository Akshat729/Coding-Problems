class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        dup_arr = sorted(arr)
        curr_rank = 1
        dic = {}

        for i in dup_arr:
            if i not in dic:
                dic[i] = curr_rank
                curr_rank += 1
                
        for i in range(len(arr)):
            arr[i] = dic[arr[i]]

        return arr
        
        

        