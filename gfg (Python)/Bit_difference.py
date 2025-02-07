#User function Template for python3

class Solution:
    ##Complete this function
    # Function to find number of bits needed to be flipped to convert A to B
    def countBitsFlip(self, a, b):
        ##Your code here
        bits = a ^ b
        count = 0
        
        while(bits):
            count += bits % 2
            bits //= 2
            
        return count
