# Longest Palindrome

# This solution leverages the property that palindromes are mirrored through the middle;
# this means that any character left of the middle also appears right of the middle, and one middle character can appear once.
# In the solution we iterate over the string, keeping track of each character.
# Once we find a duplicate character of a previous character, we can add them both to the palindrome.
# At the end, if there are any remaining non-duplicate characters we can add one to the middle of our palindrome
class Solution:
    def longestPalindrome(self, s: str) -> int:
        res = 0 # Length of the longest palindrome
        singleLetters = set() # Set can be used, since duplicates are added to length of res and then removed from the set
        for char in s:
            if char in singleLetters: 
                res += 2 # If a duplicate is found, both chars can be used in the palindrome
                singleLetters.remove(char)
            else:
                singleLetters.add(char)

        if singleLetters: res += 1 # If there are any single letters left, we can put one in the middle of the palindrome
        return res