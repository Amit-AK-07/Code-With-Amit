#User function Template for python3

class Solution:
    #Function to check if a is a subset of b.
    def isSubset(self, a, b):
        # Your code here
        mp = {}
        
        for num in a:
            mp[num] = mp.get(num, 0) + 1
            
            
        for num in b:
            mp[num] = mp.get(num, 0) - 1
            
            
        for num in b:
            if mp[num]  < 0:
                return False
                
        return True
    
    
    

