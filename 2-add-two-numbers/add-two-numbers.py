class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        # Create a dummy node to act as the head of the result list
        dummy = ListNode(0)
        current = dummy
        carry = 0
        
        # Iterate while there are nodes in either list or a remaining carry
        while l1 or l2 or carry:
            # Get values from nodes, or 0 if the list has reached its end
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0
            
            # Calculate sum and new carry
            total = val1 + val2 + carry
            carry = total // 10
            
            # Create a new node with the single-digit result
            current.next = ListNode(total % 10)
            
            # Advance pointers
            current = current.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
            
        return dummy.next