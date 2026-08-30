# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        nodeList = []
        traverse = head
        while traverse is not None:
            nodeList.append(traverse)
            traverse = traverse.next

        end = nodeList[-1]

        listLength = len(nodeList)

        traverse = head

        print(nodeList)

        print(listLength)

        while end != traverse and traverse.next != end:
            memory = traverse.next
            traverse.next = end
            end.next = memory
            nodeList.pop()
            end = nodeList[-1]
            end.next = None
            traverse = memory


        # for i in range(listLength/2)
