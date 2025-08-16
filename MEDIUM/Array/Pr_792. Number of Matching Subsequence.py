from collections import defaultdict

class Solution:
    def numMatchingSubseq(self, s, words):
        waiting = defaultdict(list)
        
        # Initialize: each word is waiting for its first character
        for word in words:
            waiting[word[0]].append(iter(word[1:]))
        
        count = 0
        for c in s:
            # Take current bucket of words waiting for c
            advance = waiting[c]
            waiting[c] = []
            for it in advance:
                nxt = next(it, None)
                if nxt:  # still has more chars to match
                    waiting[nxt].append(it)
                else:    # word finished
                    count += 1
        return count
