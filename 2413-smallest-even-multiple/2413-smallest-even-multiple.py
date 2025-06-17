class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """
        multiple = 0
        
        if n == 1:
            return 2*n

        for i in range(2, n+1):
            if i % 2 == 0 and i % n == 0:
                multiple = i
            else:
                multiple = 2*n
                
        return multiple