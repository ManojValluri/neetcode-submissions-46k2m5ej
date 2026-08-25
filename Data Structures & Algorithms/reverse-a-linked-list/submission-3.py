# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        traverse = head
        memory = None
        assignNew = None
        while(traverse is not None):
            assignNew = traverse.next
            traverse.next = memory
            memory = traverse
            traverse = assignNew
        return memory