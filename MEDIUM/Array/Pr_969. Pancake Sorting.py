class Solution:
    def pancakeSort(self, arr):
        res = []
        n = len(arr)

        for size in range(n, 1, -1):
            # Find index of the max number within first "size" elements
            max_idx = arr.index(max(arr[:size]))

            if max_idx == size - 1:
                continue  # already in correct place

            # Step 1: Flip max element to front if not already there
            if max_idx != 0:
                arr[:max_idx+1] = reversed(arr[:max_idx+1])
                res.append(max_idx + 1)

            # Step 2: Flip max element from front to its correct position
            arr[:size] = reversed(arr[:size])
            res.append(size)

        return res


# Example usage
sol = Solution()
print(sol.pancakeSort([3, 2, 4, 1]))  # Example output: [3,4,2,3,2]
print(sol.pancakeSort([1, 2, 3]))     # Example output: []
