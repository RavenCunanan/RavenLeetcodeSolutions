class Solution(object):
    def minFlips(self, a, b, c):
        flips = 0
        while a > 0 or b > 0 or c > 0:
            a_bit = a & 1
            b_bit = b & 1
            c_bit = c & 1

            if (a_bit|b_bit) != c_bit:
                if c_bit == 1:
                    flips+=1 # Either a or b is 0, both need to be 1 in OR
                else:
                    flips += a_bit + b_bit # Need to flip any 1s to 0s
            
            a >>= 1
            b >>= 1
            c >>= 1
        return flips
