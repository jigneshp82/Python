from contextlib import nullcontext
from typing import List
from Linklist import ListNode, linklist

class MergeList:

    def Merge2SortedList(self, head1:ListNode, head2:ListNode)-> ListNode:

        dummy = ListNode()
        prev = dummy

        while  head1 and head2:
            if head1.data < head2.data:
                prev.next = head1
                head1 = head1.next
            else:
                prev.next = head2
                head2 = head2.next
            prev = prev.next

        if head1:
            prev.next = head1
        
        if head2:
            prev.next = head2

        return dummy.next

    def mergeklists(self, lists:list[ListNode], s:int, e:int)-> ListNode:
        if s > e: return None
        if s == e: return lists
        mid = (s + e) // 2
        rightlist = self.mergeklists(lists,s, mid)
        leftlist = self.mergeklists(lists,mid + 1, e)
        return (self.Merge2SortedList(rightlist,leftlist))

    def mergeksortedlists(self, lists:list[ListNode]) -> ListNode:
        return self.mergeklists(lists,0, len(lists) -1)



    def printlist(self, head:ListNode):
        el = []
        while head:
            el.append(head.data)
            head = head.next
        print (el)
            

s = MergeList()        

newlist1 = linklist(1)
newlist1.appendlist(4)
newlist1.appendlist(7)
newlist1.appendlist(8)

newlist2 = linklist(2)
newlist2.appendlist(3)
newlist2.appendlist(5)
newlist2.appendlist(6)
newlist2.appendlist(9)

newList3 =linklist(5)
newList3.appendlist(10)
newList3.appendlist(11)

s.printlist(newlist1.head)
s.printlist(newlist2.head)

mergelist = s.Merge2SortedList(newlist1.head, newlist2.head)
s.printlist(mergelist)
mergelist = s.Merge2SortedList(mergelist,newList3.head)
s.printlist(mergelist)