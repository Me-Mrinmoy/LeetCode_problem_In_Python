# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:

        queue = deque()

        def removeNode(parent, leftChild, rightChild, valToDelete):
            if leftChild and leftChild.val == valToDelete:
                parent.left = None
                queue.append(leftChild.left)
                queue.append(leftChild.right)
                return True
            elif rightChild and rightChild.val == valToDelete:
                parent.right = None
                queue.append(rightChild.left)
                queue.append(rightChild.right)
                return True
            res = False
            if leftChild:
                res = res or removeNode(leftChild, leftChild.left, leftChild.right, valToDelete)
            if rightChild:
                res = res or removeNode(rightChild, rightChild.left, rightChild.right, valToDelete)
            return res
        
        queue.append(root)
        i = 0
        while i < len(to_delete):
            valToDelete = to_delete[i]
            currRoot = queue.popleft()
            if currRoot:
                if currRoot.val == valToDelete:
                    queue.append(currRoot.left)
                    queue.append(currRoot.right)
                    i += 1
                else:
                    if removeNode(currRoot, currRoot.left, currRoot.right, valToDelete):
                        i += 1
                    queue.append(currRoot)

        return filter(lambda x: x, queue)
