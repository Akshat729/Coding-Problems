class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        seq = [*range(1,10)]
        res = []
        for i in seq:
            d = i % 10
            if d < 9:
                seq.append(i * 10 + d + 1)

        for i in seq:
            if i < low:
                continue
            if i > high:
                break
            res.append(i)
        return res
        

        