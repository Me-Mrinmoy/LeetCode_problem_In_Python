class Solution(object):
    def expressiveWords(self, S, words):
        def check(word):
            i = j = 0
            while i < len(S) and j < len(word):
                if S[i] != word[j]:
                    return False
                ch = S[i]
                cntS = cntW = 0
                while i < len(S) and S[i] == ch:
                    cntS += 1
                    i += 1
                while j < len(word) and word[j] == ch:
                    cntW += 1
                    j += 1
                if cntS < cntW:
                    return False
                if cntS < 3 and cntS != cntW:
                    return False
            return i == len(S) and j == len(word)

        ans = 0
        for w in words:
            if check(w):
                ans += 1
        return ans
