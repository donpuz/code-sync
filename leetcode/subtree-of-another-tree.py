# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # we can short circuit here because we know a null subRoot is always a subTree. however, problem states subroot is never null, so no need.
        # if not subRoot:
        #     return True

        # if root is null but subRoot is not, return False (base case for isSubtree)
        if not root and subRoot:
            return False

        # traverse and check whether current root is same as subRoot, return True if True
        if self.isSame(root, subRoot):
            return True
        
        # else, call isSubtree on root.left and root.right (return root.left or root.right)
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)


    
    def isSame(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root and not subRoot:
            return True

        
        if root and subRoot and root.val == subRoot.val:
            return self.isSame(root.left, subRoot.left) and self.isSame(root.right, subRoot.right)
        
        return False