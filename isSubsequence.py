class Solution(object):
    def isSubsequence(self, s, t):
        #initialize two pointers for s and t
        i,j=0,0

        #Loop through both strings
        while i<len(s) and j<len(t):
            #If characters match, move pointer i
            if s[i]==t[j]:
                i+=1
            #always move pointerj
            j+=1
        
        return i == len(s)
