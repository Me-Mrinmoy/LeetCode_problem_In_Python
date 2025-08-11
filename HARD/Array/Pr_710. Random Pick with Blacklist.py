import random

class Solution:

    def __init__(self, n, blacklist):
        self.bound = n - len(blacklist)  # allowed pick range
        blackset = set(blacklist)

        # Find replacement numbers in the upper range
        self.mapping = {}
        last = n - 1
        for b in blacklist:
            if b < self.bound:
                while last in blackset:
                    last -= 1
                self.mapping[b] = last
                last -= 1

    def pick(self):
        # pick from [0, bound-1]
        idx = random.randint(0, self.bound - 1)
        return self.mapping.get(idx, idx)
