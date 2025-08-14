from collections import deque

class Solution:
    def openLock(self, deadends, target):
        dead_set = set(deadends)
        start = "0000"
        
        # If start is deadend
        if start in dead_set:
            return -1
        
        # BFS
        queue = deque([(start, 0)])
        visited = {start}
        
        while queue:
            state, steps = queue.popleft()
            
            if state == target:
                return steps
            
            for next_state in self.get_neighbors(state):
                if next_state not in visited and next_state not in dead_set:
                    visited.add(next_state)
                    queue.append((next_state, steps + 1))
        
        return -1
    
    def get_neighbors(self, state):
        neighbors = []
        for i in range(4):
            digit = int(state[i])
            # Rotate up
            up = (digit + 1) % 10
            # Rotate down
            down = (digit - 1) % 10
            neighbors.append(state[:i] + str(up) + state[i+1:])
            neighbors.append(state[:i] + str(down) + state[i+1:])
        return neighbors


# Example usage
deadends = ["0201","0101","0102","1212","2002"]
target = "0202"
print(Solution().openLock(deadends, target))  # Output: 6
