from collections import deque

class Solution:
    def deckRevealedIncreasing(self, deck):
        deck.sort(reverse=True)  # place back from largest to smallest
        dq = deque()
        for card in deck:
            if dq:
                dq.appendleft(dq.pop())  # reverse "move top to bottom"
            dq.appendleft(card)
        return list(dq)
