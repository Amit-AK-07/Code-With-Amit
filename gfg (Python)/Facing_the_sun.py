#User function Template for python3

class Solution:
    # Returns count buildings that can see sunlight
    def countBuildings(self, height):
        # code here
        if not height:
            return 0
            
        count = 1
        max_height = height[0]
        
        for i in height[1:]:
            if i > max_height:
                count += 1
                max_height = i
                
        return count
