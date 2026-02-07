# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # recurse on height, at each root check if |left - right| <= 1
        # if not set res to False

        # sol with nonlocal
        res = True

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

        # sol without nonlocal

        # # height, balanced (bool)
        # def dfs(root):
        #     if not root:
        #         return 0, True
            
        #     left, left_bal = dfs(root.left)
        #     right, right_bal = dfs(root.right)

        #     root_bal = left_bal and right_bal and abs(left - right) <= 1

        #     return max(left, right) + 1, root_bal

        # height, balanced = dfs(root)
        # return balanced