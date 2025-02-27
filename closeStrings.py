class Solution(object):
    from collections import Counter
    def closeStrings(self, word1, word2):
        # Check if the lengths are the same
        if len(word1) != len(word2):
            return False
        
        # Check if the sets of characters are the same
        if set(word1) != set(word2):
            return False
        
        #Get the frequency of each charcter in both words
        count1 = Counter(word1)
        count2 = Counter(word2)

        return sorted(count1.values()) == sorted(count2.values())
