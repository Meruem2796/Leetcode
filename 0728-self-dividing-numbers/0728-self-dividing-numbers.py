class Solution(object):
    def selfDividingNumbers(self, left, right):
        """
        :type left: int
        :type right: int
        :rtype: List[int]
        """
        
        self_dividing_nums = []

        for num in range(left, right + 1):
            if "0" in str(num):
                continue
            if all(num % digit == 0 for digit in map(int, str(num))):
                self_dividing_nums.append(num)

        return self_dividing_nums