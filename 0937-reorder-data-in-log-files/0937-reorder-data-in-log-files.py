class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        
        def custom_sort(log):
            identifier, content = log.split(" ", 1)
            return (0, content, identifier) if content[0].isalpha() else (1,)

        return sorted(logs, key=custom_sort)
