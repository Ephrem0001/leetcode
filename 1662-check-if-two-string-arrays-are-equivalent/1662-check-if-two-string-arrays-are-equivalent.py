class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        result1 = "".join(word1)
        result2 = "".join(word2)
        return result1==result2

