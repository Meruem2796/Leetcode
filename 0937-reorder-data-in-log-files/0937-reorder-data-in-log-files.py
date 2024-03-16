class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        
        digit_logs = []
        letter_logs = []

        for log in logs:
            if log.split()[1].isdigit():  # Check if second part is a digit
                digit_logs.append(log)
            else:
                letter_logs.append(log)

        # Sort letter logs based on content after identifier
        letter_logs.sort(key=lambda x: (x.split()[1:], x.split()[0]))

        return letter_logs + digit_logs
