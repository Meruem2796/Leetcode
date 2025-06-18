class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_set = set(nums)
        full_set = set(range(len(nums) + 1))

        return next(iter(full_set - num_set))
