# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def bstFromPreorder(self, preorder):
        self.index = 0

        def buildBST(bound):
            if self.index == len(preorder) or preorder[self.index] > bound:
                return None

            root_val = preorder[self.index]
            self.index += 1
            root = TreeNode(root_val)

            root.left = buildBST(root_val)
            root.right = buildBST(bound)

            return root

        return buildBST(float('inf'))
