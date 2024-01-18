class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """
        separator = ""
        result1 = separator.join(word1)
        result2 = separator.join(word2)
        if result1==result2:
            return True
        else:
            return False