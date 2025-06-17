class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        list = []
        list1 = nums[:n]
        list2 = nums[n:]

        for i,j in zip(list1, list2):
            list.append(i)
            list.append(j)
            
        return list