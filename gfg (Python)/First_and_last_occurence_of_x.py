#User function Template for python3


class Solution:
    def find(self, arr, x):
        
        # code here
        n=len(arr)
        ans = []
        
        for i in range(n):
            if arr[i]==x:
                ans.append(i)
        if ans:
            return [ans[0],ans[-1]]
        else:
            return [-1,-1]