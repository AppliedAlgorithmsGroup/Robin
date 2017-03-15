# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumNumbers(self, root):
        
        if root == None:
            return 0

        queue = []
        result = 0
        queue.append((root, 0))
        
        while len(queue) != 0:

            node, c_sum = queue.pop(0)
            c_sum += node.val
            if node.left == None and node.right == None:
                
                result += c_sum
            else:
                if node.left != None:
                    queue.append(( node.left, c_sum * 10))
                if node.right != None:
                    queue.append(( node.right, c_sum * 10))
            
        return(result)
        
        
        """
        :type root: TreeNode
        :rtype: int
        """