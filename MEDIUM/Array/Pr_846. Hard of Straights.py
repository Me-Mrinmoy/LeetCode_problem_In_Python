from collections import Counter

class Solution:
    def isNStraightHand(self, hand, groupSize):
        n = len(hand)
        if n % groupSize != 0:
            return False
        
        count = Counter(hand)
        
        for card in sorted(count):  # always start from the smallest card
            while count[card] > 0:
                # try to form a group [card, card+1, ..., card+groupSize-1]
                for i in range(groupSize):
                    if count[card + i] == 0:
                        return False
                    count[card + i] -= 1
        return True
