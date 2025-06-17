class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        if n % 2 != 0:
            output = 2 * n
        else:
            output = n

        return output
