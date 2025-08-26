from collections import Counter

class Solution:
    def wordSubsets(self, words1, words2):
        # Step 1: build the maximum frequency requirement from words2
        max_req = Counter()
        for w in words2:
            freq = Counter(w)
            for c in freq:
                max_req[c] = max(max_req[c], freq[c])
        
        # Step 2: check each word in words1
        res = []
        for w in words1:
            freq = Counter(w)
            ok = True
            for c in max_req:
                if freq[c] < max_req[c]:
                    ok = False
                    break
            if ok:
                res.append(w)
        
        return res
