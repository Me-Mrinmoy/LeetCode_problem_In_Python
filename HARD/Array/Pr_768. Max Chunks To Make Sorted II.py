class Solution:
    def maxChunksToSorted(self, arr):
        n = len(arr)
        
        left_max = [0] * n
        right_min = [0] * n
        
        # Build left_max
        left_max[0] = arr[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i-1], arr[i])
        
        # Build right_min
        right_min[-1] = arr[-1]
        for i in range(n-2, -1, -1):
            right_min[i] = min(right_min[i+1], arr[i])
        
        # Count chunks
        chunks = 1
        for i in range(n-1):
            if left_max[i] <= right_min[i+1]:
                chunks += 1
        
        return chunks


# Example usage
print(Solution().maxChunksToSorted([5,4,3,2,1]))  # Output: 1
print(Solution().maxChunksToSorted([2,1,3,4,4]))  # Output: 4
