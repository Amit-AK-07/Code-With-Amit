#User function Template for python3

class Solution:
    def minimumStep (self, n):
        #complete the function here
        ans = 0
        while n != 1:
            if n % 3 == 0:
                ans += 1
                n //= 3
            else:
                n -= 1
                ans += 1
        return ans