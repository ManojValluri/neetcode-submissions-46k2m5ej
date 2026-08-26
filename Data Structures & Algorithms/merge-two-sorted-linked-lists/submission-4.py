# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        mergedListHead = ListNode()
        traverseMerge = mergedListHead
        while list1 is not None or list2 is not None:
            if list2 is not None and list1 is not None and list2.val > list1.val:
                traverseMerge.val = list1.val
                list1 =  list1.next

            elif list2 is not None and list1 is not None and list2.val <= list1.val:
                traverseMerge.val = list2.val
                list2 = list2.next
            
            elif list2 is None:
                traverseMerge.val = list1.val
                list1 =  list1.next

            elif list1 is None:
                traverseMerge.val = list2.val
                list2 =  list2.next
            
            if list1 is not None or list2 is not None:
                traverseMerge.next = ListNode()
                traverseMerge = traverseMerge.next

        return mergedListHead
        
