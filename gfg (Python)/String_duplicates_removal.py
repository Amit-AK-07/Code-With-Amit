#User function Template for python3
class Solution:

    
    def removeDuplicates(self, s):
        # code here
        result = ""
        for i in s:
            if i not in result:
                result += i
                
        return result
        