from collections import deque

class Solution:
    def slidingPuzzle(self, board):
        # Convert board to string
        start = ''.join(str(num) for row in board for num in row)
        target = "123450"
        
        # Neighbor mapping for each position of '0'
        neighbors = {
            0: [1, 3],
            1: [0, 2, 4],
            2: [1, 5],
            3: [0, 4],
            4: [1, 3, 5],
            5: [2, 4]
        }
        
        # BFS setup
        queue = deque([(start, 0)])
        visited = {start}
        
        while queue:
            state, moves = queue.popleft()
            if state == target:
                return moves
            
            zero_pos = state.index('0')
            for nei in neighbors[zero_pos]:
                new_state = list(state)
                # Swap 0 with neighbor
                new_state[zero_pos], new_state[nei] = new_state[nei], new_state[zero_pos]
                new_state_str = ''.join(new_state)
                
                if new_state_str not in visited:
                    visited.add(new_state_str)
                    queue.append((new_state_str, moves + 1))
        
        return -1


# Example usage
print(Solution().slidingPuzzle([[1,2,3],[4,0,5]]))  # Output: 1
print(Solution().slidingPuzzle([[1,2,3],[5,4,0]]))  # Output: -1
print(Solution().slidingPuzzle([[4,1,2],[5,0,3]]))  # Output: 5
