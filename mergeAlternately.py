class Solution(object):
    def mergeAlternately(self, word1, word2):
        merged=[]
        i,j=0,0
        #add one letter at a time use different iterators for each string
        while i<len(word1) and j<len(word2):
            merged.append(word1[i])
            merged.append(word2[j])
            i+=1
            j+=1
        #add leftover word slice of the longer string
        if i<len(word1):
            merged.append(word1[i:])
        if j<len(word2):
            merged.append(word2[j:])
        #return the the joined list
        return ''.join(merged)
