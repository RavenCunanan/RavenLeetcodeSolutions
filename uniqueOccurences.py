class Solution(object):
    def uniqueOccurrences(self, arr):
        # Use a dictionary to count occurrences of each value
        occurrence_count={}
        
        # Count occurrences of each element in the array
        for num in arr:
            if num in occurrence_count:
                occurrence_count[num] += 1
            else:
                occurrence_count[num] = 1
        
        # Use a set to check if all occurrence counts are unique
        unique_counts = set(occurrence_count.values())

        # If the number of unique counts equals the number of unique values, return True
        return len(unique_counts) == len(occurrence_count)
