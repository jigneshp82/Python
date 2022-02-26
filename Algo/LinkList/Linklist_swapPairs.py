"""
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
from Linklist import ListNode, linklist
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        switch = 1
        cur = head
        prev = None
        h = None
        while cur:
            if switch:
                temp = cur.next
                cur.next = prev
                prev = cur
                cur = temp
                switch = 1
            else:
                prev = cur
                cur = cur.next
                switch = 0
            if h == None:
                h= prev

        return h
    
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        prev = None
        while cur:
            temp = cur.next
            cur.next = prev
            prev = cur
            cur = temp
        return prev
    
    def DisplayList(self,head:ListNode):
        l = []
        while head:
            l.append(head.data)
            head =head.next
        print (l)

s = Solution()
l = linklist(0)
l.appendlist(1)
l.appendlist(2)
l.appendlist(3)
l.appendlist(4)
s.DisplayList(l.head)
l.head = s.swapPairs(l.head)
s.DisplayList(l.head)
