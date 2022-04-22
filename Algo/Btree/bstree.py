class Node: 
    def __init__(self,val:int, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

    def insert(self, val):
        if self.val:
            if self.val > val:
                if self.left:
                    self.left.insert(val)
                else:
                    self.left = Node(val)
            if self.val < val:
                if self.right:
                    self.right.insert(val)
                else:
                    self.right = Node(val)

    def preInsert(self,val):
        if self.val:
            if self.left:
                self.preInsert(val)
            if self.right:
                self.preInsert(val)
        

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.val, end = ' ')
        if self.right:
            self.right.inorder()
    

    def preorder(self):
        print(self.val, end = ',')
        if self.left:
            self.left.preorder()      
        if self.right:
            self.right.preorder()

    def preorerList(self,L:list):
        if self.val:
            L.append(self.val)
        if self.left:
            self.left.preorerList(L)
        if self.right:
            self.right.preorerList(L)
        
        return(L)
    
    def isCousine2(self, x:int, y:int) ->bool:
        def dfs(node: Node, par:Node, dep : int, v:int):
            if not node: return
            if node.val == v:
                return node, v
            else:
                return dfs(node.left,node,dep+1, v) or dfs(node.right, node, dep+1, v)
            

        Xp, Xd = dfs(self, None, 0, x)
        Yp, Yd = dfs(self, None, 0, y)

        return (Xd == Yd and Xp != Yp)

    def isCousine(self, x:int, y:int)-> bool:
        xp = None
        yp = None
        xd = 0
        yd = 0
        xp,xd = self.helper( None, xd, x)
        print ('--')
        yp,yd = self.helper(None,  yd, y)
        return  True if (xd == yd and xp != yp) else False
            
    
    def helper(self, parent, depth: int, K:int):
        if not self : 
            print ('**')
            return 
        if self.val == K:
            return self, depth
        else:
            print (self.val)
            if self.left:
                print ('l')
                return(self.left.helper(self,depth+1, K))
            elif self.right:
                print ('r')
                return (self.right.helper(self,depth+1, K))
    
    def sumLeft(self,root)->int:
        def helpermethod(root, Sum:int)->int:
                if root.left:
                    Sum = Sum + root.left.val
                    helpermethod(root.left,Sum)
                if root.right:
                    helpermethod(root.right, Sum)
            
        
        if root:
            return(helpermethod(root,0))
            
        
        
             


if __name__ == '__main__':
    n = Node(3)
    n.insert(2)
    n.insert(1)
    n.insert(4)
    n.insert(5)


    n.preorder()
    print ('--')
    xx = n.isCousine2(1,5)
