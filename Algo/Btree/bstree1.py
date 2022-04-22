from tkinter.tix import Tree

from sklearn import tree


class TreeNode:
    def __init__(self, val = 0, left = None, right = None):
        self.val = val
        self.right = right
        self.left = left

    
class BST:
    def __init__(self, val):
        self.root = TreeNode(val)

    
    def insertNode(self, root, val):
        if root:
            if val < root.val:
                if root.left : self.insertNode(root.left,val)
                else: root.left = TreeNode(val)
            if val > root.val:
                if root.right : self.insertNode(root.right, val)
                else: root.right = TreeNode(val)
            
    

    
    def inorder(self, root: TreeNode):
        if root:
            self.inorder(root.left)
            print (root.val, end = " ")
            self.inorder(root.right)

    def preorder(self, root:TreeNode):
        if root:
            print (root.val, end= " ")
            self.preorder(root.left)
            self.preorder(root.right)

    def postorder(self, root: TreeNode):
        if root:
            self.postorder(root.right)
            print(root.val, end = " ")
            self.postorder(root.left)
            
    def convertBSTGreattree(self, root: TreeNode) -> TreeNode:
        def dfs(root: TreeNode, key : int):            
            if root:
                key = dfs(root.right, key)
                root.val += key
                key = dfs(root.left, root.val)
                return key
            return key

        dfs(root, 0)
        return root



tree = BST(4)
tree.insertNode(tree.root,1)
tree.insertNode(tree.root,0)
tree.insertNode(tree.root,2)
tree.insertNode(tree.root,3)
tree.insertNode(tree.root,6)
tree.insertNode(tree.root,5)
tree.insertNode(tree.root,7)
tree.insertNode(tree.root,8)

print (" inoder : ", end = " ")
tree.inorder(tree.root)
print("\n prerder: ", end = " ")
tree.preorder(tree.root)
print("\n postorder: ", end = " ")
tree.postorder(tree.root)
print ("\n")
tree.convertBSTGreattree(tree.root)
tree.postorder(tree.root)

