#User function Template for python3
class Solution:
    def isPalindrome(self, s: str) -> bool:
        # code here
        start = 0
        end = len(s) - 1
        
        while start < end:
            if(s[start] != s[end]):
                return False
            start += 1
            end -= 1
                
        return True
