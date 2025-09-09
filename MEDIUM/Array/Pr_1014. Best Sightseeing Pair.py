class Solution:
    def maxScoreSightseeingPair(self, a: List[int]) -> int:
        return reduce(lambda p,v:(max(p[0],p[1]+v),max(p[1],v)-1),a,(0,0))[0]
