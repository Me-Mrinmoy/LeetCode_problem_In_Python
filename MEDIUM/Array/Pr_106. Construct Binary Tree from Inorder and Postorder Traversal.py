class Solution:
    def buildTree(self, inorder, postorder):
        
        inorder_index_map = {value: idx for idx, value in enumerate(inorder)}

        
        def helper(in_left, in_right):
            
            if in_left > in_right:
                return None

            
            root_val = postorder.pop()
            root = TreeNode(root_val)

            
            index = inorder_index_map[root_val]

            
            root.right = helper(index + 1, in_right)

            
            root.left = helper(in_left, index - 1)

            return root

        
        return helper(0, len(inorder) - 1)
