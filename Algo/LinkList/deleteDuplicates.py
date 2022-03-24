
"""
82. Remove Duplicates from Sorted List II
Medium

5309

160

Add to List

Share
Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

 

Example 1:


Input: head = [1,2,3,3,4,4,5]
Output: [1,2,5]
Example 2:


Input: head = [1,1,1,2,3]
Output: [2,3]
 

Constraints:

The number of nodes in the list is in the range [0, 300].
-100 <= Node.val <= 100
The list is guaranteed to be sorted in ascending order.

"""
#Definition for singly-linked list.
from Linklist import linklist,ListNode

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummy = prev =  ListNode()
        dummy.next = head
        while head and head.next:
            if head.val == temp.val:
                while head and head.val == head.next.val:
                    head = head.next
                head = head.next
                prev.next = head
            else:
                prev = prev.next
                head = head.next

        return dummy.next
    def delelement(self,head:ListNode, e:int) -> ListNode:
        dummy = tail = ListNode()
        tail.next = head
        while head:
            if head.data == e:
                if head == dummy:
                    dummy.next = head.next
                    tail = head.next
                else:
                    tail.next = head.next
            head = head.next
            tail = head
        return dummy.next

l1 = linklist(1)
l1.appendlist(2)
l1.appendlist(3)
l1.appendlist(4)
l1.appendlist(5)
l1.display()
s = Solution()
s.delelement(l1.head, 2)
l1.display()
            
        
            
        