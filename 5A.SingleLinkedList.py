# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        
        slow = head
        if head is not None and head.next is not None:
            fast = head.next
        else:
            return False
            
        while slow is not None and fast is not None and fast.next is not None:
            if (slow == fast):
                return True
            else:
                slow = slow.next
                fast = fast.next.next
        
        return False
            
        
        """
        :type head: ListNode
        :rtype: bool
        """
        