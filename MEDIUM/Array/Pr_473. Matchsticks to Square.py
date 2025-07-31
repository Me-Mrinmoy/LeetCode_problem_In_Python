class Solution:
    def makesquare(self, matchsticks):
        total = sum(matchsticks)
        
        if total % 4 != 0:
            return False
        
        side = total // 4
        matchsticks.sort(reverse=True)  # optimization: try longer sticks first
        sides = [0] * 4
        
        def backtrack(index):
            if index == len(matchsticks):
                # All sticks used, check if all sides are equal
                return all(s == side for s in sides)
            
            for i in range(4):
                if sides[i] + matchsticks[index] <= side:
                    sides[i] += matchsticks[index]
                    if backtrack(index + 1):
                        return True
                    sides[i] -= matchsticks[index]  # backtrack

                # If this side is still 0 after trying, no need to try other empty sides (prune)
                if sides[i] == 0:
                    break
                    
            return False
        
        return backtrack(0)
