# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # we can reverse a list by creating a stack, tracking every node visited,
        # then, when we reach the end, we unwind the stack and create a new list,
        # in reverse order
        '''stack = []
        
        while head.next is not None:
            #print (head.val)
            stack.append(head.val)
            head = head.next
        # at this point, we have a stack with all the items from the linked list
        # now, pop them back, one by one, into a new ListNode
        head = stack.pop()
        while stack.next is not None:
            head.next = '''
        # ... or we can reverse it in place by pointing the nodes backwards while iterating over the list
        prev = None
        current = head
        while current is not None:
            # store the value of Next node
            next = current.next
            # point the next pointer backwards (None in first case, and rear node in oher cases)
            current.next = prev
            # go next to the next node
            prev = current
            current = next
        head = prev
        return head
