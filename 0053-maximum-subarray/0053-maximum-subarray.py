class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = float('-inf')  # Initialiser à une valeur négative infinie
        current_sum = 0  # Somme courante du sous-tableau

        for num in nums:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
            
        return max_sum
