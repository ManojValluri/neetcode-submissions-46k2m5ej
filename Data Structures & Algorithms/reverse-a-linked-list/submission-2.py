# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        traverse = head
        # print(traverse.next)
        # print(traverse.val)
        assignTemp = ListNode()
        memory = None
        while(traverse is not None):
            assign = traverse
            traverse = traverse.next
            assign.next = memory
            memory = assign
        head = traverse
        return memory
