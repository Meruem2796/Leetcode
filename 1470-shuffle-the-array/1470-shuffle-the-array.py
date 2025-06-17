class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        output = []
        first_list = nums[:n]
        scnd_list = nums[n:]
        for i, j in zip(first_list, scnd_list):
            output.append(i)
            output.append(j)

        return output
