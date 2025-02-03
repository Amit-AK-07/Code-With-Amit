#User function Template for python3

class Solution:
    def countOddEven(self, arr):
        #Code here
        odd_count = 0;
        even_count = 0
        n = len(arr)
        
        for i in range(n):
            if (arr[i] % 2 == 0):
                odd_count += 1
            else:
                even_count += 1
                
        return even_count, odd_count
