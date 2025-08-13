from collections import Counter

class Solution:
    def shortestCompletingWord(self, licensePlate, words):
        need = Counter(ch.lower() for ch in licensePlate if ch.isalpha())
        ans = None
        for w in words:
            if not (need - Counter(w)):   # w covers all required letters/counts
                if ans is None or len(w) < len(ans):
                    ans = w               # ties keep the first seen (earliest)
        return ans
