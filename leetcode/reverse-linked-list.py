# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 1 to point at none
        # need to keep reference to next before setting 1 to point to none (or prev node)
        
        # prev = None
        # curr = head

        # at each iteration:
        # set temp to curr.next
        # set curr.next to prev
        # set prev = curr
        # curr = temp

        # 1 --> 2 --> 3 --> None
        # 1 --> None , 2 --> 3 --> None | prev = 1, curr = 2
        # 2 --> 1 --> None , 3 --> None | prev = 2, curr = 3
        # 3 --> 2 --> 1 --> None , None | prev = 3, curr = None

        prev = None
        curr = head
        while curr is not None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        return prev