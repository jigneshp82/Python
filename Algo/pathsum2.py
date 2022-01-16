from bstree import Node as Node
class Solution:
     def pathSum(self, root: Node, targetSum: int) -> int:
        def checkpathsum(root, targetsum)->bool:
            if root:
                if root.val < targetSum:
                    checkpathsum(root.left,targetSum - root.val)
                    checkpathsum(root.right, targetSum- root.val)
                elif root.val == targetSum:
                    return True
                else:
                    return False
            return False
        def helper(root:Node, target:sum, cnt:int)-> int:
            if root:
                if root.val == targetSum:
                    cnt +=1
                if root.val < targetSum and checkpathsum(root,targetSum):
                    return True

        
        