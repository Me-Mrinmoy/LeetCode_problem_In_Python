# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sortedArrayToBST(self, nums):
        if not nums:
            return None
        
        # Find the middle index
        mid = len(nums) // 2
        
        # The middle element becomes the root
        root = TreeNode(nums[mid])
        
        # Recursively build the left subtree and right subtree
        root.left = self.sortedArrayToBST(nums[:mid])
        root.right = self.sortedArrayToBST(nums[mid + 1:])
        
        return root

# Example usage
solution = Solution()
nums1 = [-10, -3, 0, 5, 9]
nums2 = [1, 3]
result1 = solution.sortedArrayToBST(nums1)
result2 = solution.sortedArrayToBST(nums2)

# Function to print the tree in a structured way
def print_tree(root):
    if not root:
        return "null"
    return "{}({},{})".format(root.val, print_tree(root.left), print_tree(root.right))

# Print the results
print(print_tree(result1))  # Output should represent a height-balanced BST for nums1
print(print_tree(result2))  # Output should represent a height-balanced BST for nums2
