#User function Template for python3
class Solution:
    def removeVowels(self, s):
        # code here
        ans  = ""
        vowels=['a','e','i','o','u']
        
        for i in s:
            if i not in vowels:
                ans += i
        return ans
