class Solution:
    def findSecretWord(self, words, master):
        def match(w1, w2):
            """Return number of matching positions between two words."""
            return sum(a == b for a, b in zip(w1, w2))
        
        for _ in range(10):  # we can guess at most 10 times (sometimes 30)
            count = {}
            for w1 in words:
                for w2 in words:
                    if w1 != w2:
                        m = match(w1, w2)
                        count[w1] = count.get(w1, 0) + (m == 0)
            
            # pick the word with the least conflicts
            guess_word = min(words, key=lambda w: count.get(w, 0))
            
            matches = master.guess(guess_word)
            if matches == 6:
                return  # secret found
            
            # filter candidates
            words = [w for w in words if match(guess_word, w) == matches]
