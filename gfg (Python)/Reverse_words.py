# User function Template for python3

class Solution:
    # Function to reverse words in a given string.
    def reverseWords(self, s):
        # code here 
        words = s.split()
        
        rev_word = ' '.join(reversed(words))
        return rev_word
