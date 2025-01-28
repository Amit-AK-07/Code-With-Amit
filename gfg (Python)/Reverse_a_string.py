#User function Template for python3

def reverseString(s):
    #Write your code below to reverse s and return it
    n = len(s)
    ans = ""
    
    for i in range(n - 1, -1, -1):
        ans += s[i]
        
    return ans
