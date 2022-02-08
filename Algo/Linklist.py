class ListNode:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class linklist:
    def __init__(self):
        self.head = ListNode()

    def appendlist(self,data):
        newnode = ListNode(data)
        curnode = self.head
        while curnode.next != None:
            curnode = curnode.next
        curnode.next = newnode

    def display(self):
        elements= []
        stringelement = ''
        curnode = self.head
        while curnode.next != None:
            curnode = curnode.next
            elements.append(curnode.data)  
            stringelement = stringelement+str(curnode.data)
            if curnode.next != None:
                stringelement = stringelement + ' -> '
        print (stringelement) 
       
    def lengthoflist(self):
        curnode = self.head
        total =0
        while curnode.next != None:
            curnode = curnode.next
            total += 1
        return(total)

    def getelement(self, index):
        curnode =self.head
        curindex = 0
        if index > self.lengthoflist() or index < 1:
            print ("Index out of range")
            return None
        while curindex < index:
            curnode = curnode.next
            curindex += 1
        return (curnode.data)

    def delelement(self, index):
        curnode = self.head
        curindex = 0

        if index > self.lengthoflist() or index < 1:
            print ("Index out of range")
            return None
        
        while curindex < index: 
            lastnode =curnode          
            curnode = curnode.next
            curindex += 1

        lastnode.next = curnode.next

    def bubblesort(self):
        curnode = self.head
        while curnode.next != None:
            curnode = curnode.next
            compnode = curnode
            while compnode.next != None:
                compnode = compnode.next
                if curnode.data > compnode.data:
                    temp = curnode.data
                    curnode.data = compnode.data
                    compnode.data = temp

            

    def meargNode(self,Node:ListNode):
        print (Node.data)
        curr = self.head
        while curr:
            curr = curr.next
            Next = curr.next
            if Node.data > Next.data:
                continue
            else:
                temp = curr.next
                curr.next = Node
                Node.next = temp
                break

"""          
mylist = linklist()
mylist.appendlist(10)
mylist.appendlist(20)
mylist.appendlist(30)
mylist.appendlist(40)
mylist.appendlist(50)
mylist.appendlist(70)
mylist.appendlist(100)
mylist.display()
mylist2 = linklist()
mylist2.appendlist(60)
mylist2.appendlist(80)
cur = mylist2.head
while cur:
    cur = cur.next
    mylist2.display()
    mylist.meargNode(cur)
mylist.display()
"""