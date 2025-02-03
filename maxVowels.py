class Solution(object):
    def maxVowels(self, s, k):
        vowels = {'a', 'e', 'i', 'o', 'u'}  # Use a set for O(1) lookups
        max_vowels = 0  # Track the maximum number of vowels in any window
        current_vowels = 0  # Track the number of vowels in the current window

        # Count vowels in the first window
        for i in range(k):
            if s[i] in vowels:
                current_vowels += 1
            if current_vowels==k:
                return k
        max_vowels = current_vowels

        # Slide the window through the string
        for i in range(k, len(s)):
            # Remove the leftmost character of the previous window
            if s[i - k] in vowels:
                current_vowels -= 1
            # Add the new character to the window
            if s[i] in vowels:
                current_vowels += 1
            # Update the maximum vowel count
            if current_vowels > max_vowels:
                max_vowels = current_vowels
            # Early exit if the maximum possible is reached
            if max_vowels == k:
                return max_vowels

        return max_vowels
