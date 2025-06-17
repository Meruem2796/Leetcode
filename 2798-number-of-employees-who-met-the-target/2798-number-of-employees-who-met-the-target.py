class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        output = 0
        for h in hours:
            if h >= target:
                output += 1
        return output
