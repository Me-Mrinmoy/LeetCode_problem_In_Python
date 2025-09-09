class Solution:
    def prefixesDivBy5(self, x: List[int]) -> List[bool]:
        n = len(x)
        prev = 0
        res = []
        for i in range(n):
            prev = ((prev<<1) + x[i])%5
            res.append(prev==0)
        return res
