class Solution:
    def maxChunksToSorted(self, arr):
        chunks = 0
        max_so_far = 0
        
        for i, num in enumerate(arr):
            max_so_far = max(max_so_far, num)
            if max_so_far == i:
                chunks += 1
                
        return chunks


# Example usage
print(Solution().maxChunksToSorted([4,3,2,1,0]))  # Output: 1
print(Solution().maxChunksToSorted([1,0,2,3,4]))  # Output: 4
