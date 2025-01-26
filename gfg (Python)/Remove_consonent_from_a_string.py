#User function Template for python3

class Solution:
    def removeConsonants(self, s):
        #complete the function here
        vowels = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
        ans = ""
        
        for i in s:
            if i in vowels:
                ans += i
        
        return ans if len(ans) != 0 else "No Vowel"
