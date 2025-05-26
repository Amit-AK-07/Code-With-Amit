#User function Template for python3

class Solution:
    
    #Function to search a given number in row-column sorted matrix.
    def searchMatrix(self, mat, x): 
    	# code here 
    	m = len(mat)
    	n = len(mat[0])
    	
    	for i in range(m):
    	    for j in range(n):
    	        if mat[i][j] == x:
    	            return True
    	return False
    	    