# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    
    def zigzagLevelOrder(self, root):
        if root == None:
            return []
        
        
        to_return = []
        queue = []
        queue.append((root,0))
        prev_level = 0
        level_result = []
    
        while (len(queue) != 0):
            # queue for BFS
            curr_t = queue.pop(0)
            curr_n = curr_t[0]
            curr_level = curr_t[1]
            
            print(curr_n.val)
            
            if prev_level != curr_level:
                to_return.append(level_result)
                level_result = []
            if curr_level % 2 == 0 :
                level_result.insert(0, curr_n.val)
                
            else:

                level_result.append(curr_n.val)
            
            
            
            # if curr_level %2 == 0:
            if curr_n.right != None:
                queue.append( (curr_n.right,curr_level +1) )
            if curr_n.left != None:
                queue.append( (curr_n.left,curr_level +1) )
            # else:
            #     if curr_n.left != None:
            #         queue.append( (curr_n.left,curr_level +1) )
            #     if curr_n.right != None:
            #         queue.append( (curr_n.right,curr_level +1) )
            prev_level = curr_level

                
        to_return.append(level_result)       
            
            
        return to_return
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """