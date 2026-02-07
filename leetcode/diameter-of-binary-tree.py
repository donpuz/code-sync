# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # recurse on max height, but check left + right at every node

        # sol not using nonlocal
        # def dfs(root):
        #     if not root:
        #         return 0, 0
            
        #     left, left_max = dfs(root.left)
        #     right, right_max = dfs(root.right)

        #     root_max = max(left_max, right_max, left + right)

        #     return max(left, right) + 1, root_max
        
        # max_height, diameter = dfs(root)
        # return diameter

        # sol using nonlocal

        res = 0

        def dfs(root):
            if not root:
                return 0

            left = dfs(root.left)
            right = dfs(root.right)
            
            nonlocal res
            res = max(res, left + right)

            return max(left, right) + 1
        
        dfs(root)
        return res