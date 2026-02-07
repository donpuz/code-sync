# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True

        # recurse on height, at each root check if |left - right| <= 1
        # if not set res to False

        def dfs(root):
            if not root:
                return 0
            
            left = dfs(root.left)
            right = dfs(root.right)

            nonlocal res
            res = res and abs(left - right) <= 1

            return max(left, right) + 1
        
        dfs(root)
        return res