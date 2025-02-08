#User function Template for python3

class Solution:
    
    #Function to count the number of substrings that start and end with 1.
    def binarySubstring(self,n,s):
        #code here
        count = 0
        
        for i in range(n):
            if(s[i] == '1'):
                count += 1
         
        # To find no of substrings        
        return int(count * (count - 1) / 2)
