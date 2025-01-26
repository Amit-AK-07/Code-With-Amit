#User function Template for python3

class Solution:
    def splitString(ob, S): 
        # code here 
        S1 = "" 
        S2 = ""
        S3 = ""
            
        for ch in S:
            if ch.isalpha():
                S1 += ch
            elif ch.isdigit():
                S2 += ch
            else:
                S3 += ch
                
        return S1, S2, S3
       
