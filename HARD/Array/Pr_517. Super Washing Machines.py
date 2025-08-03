class Solution:
    def findMinMoves(self, machines):
        total = sum(machines)
        n = len(machines)
        
        # If it's not divisible, return -1
        if total % n != 0:
            return -1
        
        target = total // n
        max_moves = 0
        balance = 0
        
        for load in machines:
            diff = load - target
            balance += diff
            max_moves = max(max_moves, abs(balance), diff)
        
        return max_moves
