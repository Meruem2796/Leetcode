class Solution:
    def isPalindrome(self, x: int) -> bool:
        back_x = ""
        for digit in str(x):
            back_x = digit + back_x

        if str(x) == back_x:
            return True
        else:
            return False
