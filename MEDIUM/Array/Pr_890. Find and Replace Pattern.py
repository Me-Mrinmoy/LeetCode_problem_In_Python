class Solution:
    def findAndReplacePattern(self, words, pattern):
        def matches(word, pattern):
            if len(word) != len(pattern):
                return False
            
            w2p, p2w = {}, {}
            for w, p in zip(word, pattern):
                if w in w2p and w2p[w] != p:
                    return False
                if p in p2w and p2w[p] != w:
                    return False
                w2p[w] = p
                p2w[p] = w
            return True

        return [word for word in words if matches(word, pattern)]
