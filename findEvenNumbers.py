from itertools import permutations

class Solution:
    def findEvenNumbers(self, digits):
        unique_numbers = set()  # Set to store unique numbers
        
        # Generate all 3-digit permutations
        for perm in permutations(digits, 3):
            # Skip numbers with leading zero
            if perm[0] == 0:
                continue
            # Form the number from the permutation
            num = perm[0] * 100 + perm[1] * 10 + perm[2]
            # Check if the number is even (last digit must be even)
            if num % 2 == 0:
                unique_numbers.add(num)
        
        # Return the sorted list of unique numbers
        return sorted(unique_numbers)

