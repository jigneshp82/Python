"""

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

 

Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []

"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from typing import Optional
from Linklist import ListNode,linklist

class Solution:
    def mergeNode(self,l1:linklist,n:ListNode):
        cur = l1.head
        while cur:
            cur = cur.next
            nxt = cur.next
            if n.data <= nxt.data:
                temp = cur.next
                cur.next = n
                n.next = temp
                break
        return l1

                

    def mergeKLists(self, lists: list[Optional[ListNode]]) -> Optional[ListNode]:
        l1 = lists[0]
        for l in lists[1:]:
            cur = l.head
            while cur:
                cur = cur.next
                self.mergeNode(l1,cur)
        return (l1)

        
list1 = linklist()
l1 = [1,4,5]
for v in l1:
    list1.appendlist(v)

list2 = linklist()
l2 = [1,3,4]
for v in l2:
    list2.appendlist(v)
s = Solution()
LL = [list1, list2]
node = ListNode(3)
list1.display()
s.mergeKLists(LL)
list1.display()
s.mergeNode(list1,node)
list1.display()

#print(s.mergeKLists(LL))
