class Solution(object):
    def compress(self, chars):
        write=0 #Index to write the compress result
        read=0  #Index to read through the array

        while read < len(chars):
            char=chars[read]
            count=0

            #Count consecutive occurences of the character
            while read < len(chars) and chars[read]==char:
                count +=1
                read +=1
            
            #write the character
            chars[write]=char
            write+=1

            #Write the count if greater than 1
            if count > 1:
                for digit in str(count):
                    chars[write]=digit
                    write+=1
        
        return write #new length of the modified array
