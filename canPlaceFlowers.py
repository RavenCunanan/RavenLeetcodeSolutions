class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):

        #start count
        count =0

        #check for 0 then check for left and right 0;s
        for i in range(len(flowerbed)):
            if flowerbed[i]==0:
                leftEmpty = (i==0 or flowerbed[i-1]==0)
                rightEmpty = (i==len(flowerbed)-1 or flowerbed[i+1]==0)
            #plant flower and increase count if both left and right are empty
                if(leftEmpty and rightEmpty):
                    flowerbed[i]=1
                    count+=1
        #check if enough flowers were planted
        if(count>=n):
            return True
        else:
            return False
