class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        word1 = list(word1)
        index = 1
        for i in word2:
            word1.insert(index, i)
            index += 2
        return("".join(word1))