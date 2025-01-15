class Solution(object):
    #euclidean algorithim
    def gcd(self,a,b):
        while b:
            a,b=b,a%b
        return a

    #check if the strings can be divided
    def gcdOfStrings(self, str1, str2):
       if(str1+str2 != str2+str1):
        return ""
        #use algorithim
       gcd_len=self.gcd(len(str1),len(str2))
        #return the string from the gcd slice
       return str1[:gcd_len] 
    
