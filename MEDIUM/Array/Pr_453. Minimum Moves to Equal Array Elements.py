class Solution:
    def minMoves(self, nums):
        min_num = min(nums)
        moves = sum(num - min_num for num in nums)
        return moves

# Example usage:
if __name__ == "__main__":
    sol = Solution()

    # Test case 1
    nums1 = [1, 2, 3]
    print("Input:", nums1)
    print("Minimum Moves:", sol.minMoves(nums1))  # Output: 3

    # Test case 2
    nums2 = [1, 1, 1]
    print("Input:", nums2)
    print("Minimum Moves:", sol.minMoves(nums2))  # Output: 0
