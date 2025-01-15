class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        #get greatest candy value and initialize the output list
        greatestCandy = max(candies)
        list=[]

        #check if adding extra candies gives you greatest candy value or higher, and append list with true or false
        for x in candies:
            if(x+extraCandies >= greatestCandy):
                list.append(True)
            else:
                list.append(False)
        
        return list
