class node:
    def __init__(self, data = None):
        self.data = data
        self.next = None

class linklist:
    def __init__(self):
        self.head = node()

    def appendlist(self,data):
        newnode = node(data)
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

            

    
            

mylist = linklist()
mylist.appendlist(20)
mylist.appendlist(40)
mylist.appendlist(30)
mylist.appendlist(10)
mylist.appendlist(70)
mylist.appendlist(35)
mylist.display()
mylist.delelement(3)
mylist.display()
mylist.bubblesort()
mylist.display()
