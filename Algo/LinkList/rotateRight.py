"""
61. Rotate List
Medium

4190

1241

Add to List

Share
Given the head of a linked list, rotate the list to the right by k places.

Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [4,5,1,2,3]
Example 2:


Input: head = [0,1,2], k = 4
Output: [2,0,1]
 

Constraints:

The number of nodes in the list is in the range [0, 500].
-100 <= Node.val <= 100
0 <= k <= 2 * 109
"""
# Definition for singly-linked list.

from re import I
from typing import Optional
from Linklist import linklist,ListNode

class Solution:
    def display(self, head:ListNode):
        elements= []
        if not head:
            print ('empty list')
        while head:
            elements.append(head.val)  
            head =head.next
        print (*elements,sep = ',')

    def findlen(self, head:ListNode)->int:
        i =0
        while head:
            i +=1
            head =head.next
        return i

    def rotateRight2(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        dummy = tail = ListNode()
        l = self.findlen(head)
        k = k % l
        while k:
            k -=1
            tail.next = head
            nxt = tail.next
            while nxt.next:           
                tail = tail.next
                nxt = tail.next
            tail.next = None
            nxt.next = dummy.next
            dummy.next = nxt
            head = nxt
            tail = dummy
            self.display(head)
        return head

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        l = self.findlen(head)
        k = k % l
        s =f = head
        for _ in range(k):
            f = f.next
        
        while f.next:
            s = s.next
            f = f.next
        
        newhead =s.next
        s.next = None
        f.next = head
        head = newhead

        return head

    def copyRandomList(self, head: ListNode) -> ListNode:
        dummy = tail = ListNode()
        while head:
            temp  = ListNode()
            temp.val = head.val
            temp.next = head.next
            tail.next =  temp
            tail = tail.next
            head = head.next
        return dummy.next


l1 = linklist(1)
l1.appendlist(2)
l1.appendlist(3)
l1.appendlist(4)
l1.appendlist(5)
l1.display()
print ('---')
s = Solution()
l2 = s.copyRandomList(l1.head)
s.display(l2)
s.display(s.rotateRight(l1.head, 20000013))


        
