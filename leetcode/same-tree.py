# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # level order traversal and compare each node

        # separate queues?
        p_queue = [p]
        q_queue = [q]

        p_visited = set()
        q_visited = set()

        while p_queue and q_queue:
            p_curr = p_queue.pop(0)
            q_curr = q_queue.pop(0)

            if p_curr and q_curr and p_curr.val != q_curr.val:
                return False

            if (p_curr and not q_curr) or (not p_curr and q_curr):
                return False
            
            if p_curr:
                p_visited.add(p_curr)
                p_queue.append(p_curr.left)
                p_queue.append(p_curr.right)
    
            if q_curr:
                q_visited.add(q_curr)
                q_queue.append(q_curr.left)
                q_queue.append(q_curr.right)
        

        if p_queue or q_queue:
            return False
        
        return True