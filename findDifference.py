class Solution(object):
    def findDifference(self, nums1, nums2):
        #Turn lists to sets
        set1=set(nums1)
        set2=set(nums2)

        #Find elements in nums1 not in nums2 and vice versa and turn sets back into lists
        diff1=list(set1-set2)
        diff2=list(set2-set1)

        return [diff1,diff2]
