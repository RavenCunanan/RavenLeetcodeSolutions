class Solution(object):
    def reverseVowels(self, s):
        
        vowels={'a','e','i','o','u','A','E','I','O','U'}
        s=list(s)
        left,right=0,len(s)-1

        while (left < right):
            if(s[left] in vowels and s[right] in vowels):
                #swap vowels if both vowels are found
                s[left],s[right]=s[right],s[left]
                #iterate
                left+=1
                right-=1
            elif s[left] not in vowels:
                left+=1
            elif s[right] not in vowels:
                right-=1
            
        return ''.join(s) #turns list into a single string
