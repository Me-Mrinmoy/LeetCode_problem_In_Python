class MajorityChecker:
    def __init__(self, arr: List[int]):
        self.loc = collections.defaultdict(list)
        for i, n in enumerate(arr):
            self.loc[n].append(i)    
        self.nums = sorted(self.loc.keys(), key = lambda n: len(self.loc[n]), reverse=True)
        
    def query(self, left: int, right: int, threshold: int) -> int:
        for n in self.nums:
            if len(self.loc[n]) < threshold: return -1
            l, r = bisect.bisect_left(self.loc[n], left), bisect.bisect_right(self.loc[n], right)
            if r - l >= threshold: return n
        return -1
