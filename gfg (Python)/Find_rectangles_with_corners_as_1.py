class Solution:    
    def ValidCorner(self,mat): 
        # Code here 
        n = len(mat)
        m = len(mat[0])
        
        for i in range(n):
            for j in range(i+1, n):
                count = 0
                
                for col in range(m):
                    if mat[i][col] == 1 and mat[j][col] == 1:
                        count += 1
                        
                        if count >= 2:
                            return True
        
        return False