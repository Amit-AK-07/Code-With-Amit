#User function Template for python3

class Solution:
    def findTwoElement( self,arr): 
        # code here
        n = len(arr)
        sum_n = n * (n + 1) // 2
        sum_sq_n = (n * (n + 1) * (2 * n + 1)) // 6
    
        # Actual sum and sum of squares
        sum_arr = sum(arr)
        sum_sq_arr = sum(x*x for x in arr)
        
        diff = sum_n - sum_arr   
        diff_sq = sum_sq_n - sum_sq_arr 

        sum_m_r = diff_sq // diff 
        
        missing = (sum_m_r + diff) // 2
        repeated = missing - diff
        
        return [repeated, missing]
