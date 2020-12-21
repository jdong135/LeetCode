# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    # Iterative
    def reverseList(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        prev = None
        cur = head
        while cur != None:
            nextNode = cur.next
            cur.next = prev
            prev = cur
            cur = nextNode
        return prev
     
     # Recursive
     def reverseListRecursive(self, head: ListNode) -> ListNode:
       if head == None or head.next == None:
              return head
          reverseListHead = self.reverseList(head.next)
          head.next.next = head
          head.next = None
          return reverseListHead
        
