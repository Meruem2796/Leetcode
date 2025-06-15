from typing import List


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result = []

        for num in range(left, right + 1):
            if self.is_self_dividing(num):
                result.append(num)

        return result

    def is_self_dividing(self, num: int) -> bool:
        """Vérifie si un nombre est auto-divisible"""
        # Les nombres à un chiffre (1-9) sont auto-divisibles par définition
        if num < 10:
            return True

        # Si le nombre contient 0, il ne peut pas être auto-divisible
        if "0" in str(num):
            return False

        # Vérifier que tous les chiffres divisent le nombre
        for digit_char in str(num):
            digit = int(digit_char)
            if num % digit != 0:
                return False

        return True
