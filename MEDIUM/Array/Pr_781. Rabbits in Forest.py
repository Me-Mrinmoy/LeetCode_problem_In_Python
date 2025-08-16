from collections import Counter

class Solution:
    def numRabbits(self, answers):
        freq = Counter(answers)
        total = 0
        for y, count in freq.items():
            group = y + 1
            groups = (count + group - 1) // group  # ceil(count/group)
            total += groups * group
        return total
