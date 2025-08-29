class Solution:
    def isAlienSorted(self, words, order):
        # Step 1: Create a mapping from char -> index
        rank = {c: i for i, c in enumerate(order)}

        # Step 2: Compare adjacent words
        for i in range(len(words) - 1):
            w1, w2 = words[i], words[i+1]
            # Compare char by char
            for j in range(min(len(w1), len(w2))):
                if w1[j] != w2[j]:
                    # Check alien order
                    if rank[w1[j]] > rank[w2[j]]:
                        return False
                    break
            else:
                # If all chars same, then length matters
                if len(w1) > len(w2):
                    return False
        return True
