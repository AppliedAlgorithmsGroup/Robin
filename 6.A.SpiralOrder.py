class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if len(matrix) == 0:
            return []
        
        first_line = list(matrix.pop(0))
        matrix_tranpose = zip(*matrix)
        result = self.spiralOrder(matrix_tranpose[::-1])
        
        return first_line + result

        