# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # 1 2 4
        # 1 3 4 x y z
        # while list1 and list2:
        # compare in here and append + move pointer forward
        # for loop to go through list1 and add
        # for loop to go through list 2 and add

        ### sus solution
        # res = None
        # res_curr = None
        # while list1 and list2:
        #     # init res
        #     if not res:
        #         if list1.val >= list2.val:
        #             res = ListNode(list2.val)
        #             list2 = list2.next
        #         else:
        #             res = ListNode(list1.val)
        #             list1 = list1.next
        #         res_curr = res # res has head, res_curr is pointing to current
        #         continue
            
        #     if list1.val >= list2.val:
        #         res_curr.next = ListNode(list2.val)
        #         list2 = list2.next
        #     else:
        #         res_curr.next = ListNode(list1.val)
        #         list1 = list1.next
            
        #     res_curr = res_curr.next

        
        # while list1 or list2:
        #     # init res
        #     if not res:
        #         if list2:
        #             res = ListNode(list2.val)
        #             list2 = list2.next
        #         else:
        #             res = ListNode(list1.val)
        #             list1 = list1.next
        #         res_curr = res # res has head, res_curr is pointing to current
        #         continue
        #     if list1:
        #         res_curr.next = ListNode(list1.val)
        #         list1 = list1.next
        #     else:
        #         res_curr.next = ListNode(list2.val)
        #         list2 = list2.next
        #     res_curr = res_curr.next
        
        # return res

        ### more optimal with dummy head

        dummy = ListNode()
        curr = dummy

        # set curr.next to list1 or list2 items,

        while list1 and list2:
            if list1.val <= list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next
        
        if list1:
            curr.next = list1
        else:
            curr.next = list2

        return dummy.next