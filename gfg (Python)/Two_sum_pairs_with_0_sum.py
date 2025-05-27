#User function Template for python3

class Solution:
    def getPairs(self, arr):
        # code here
        ret = set()
        arr.sort()
        n = len(arr)
        m = n - 1
        
        for i in range(n):
            if i >= m:
                break
            
            while arr[m] >- arr[i]:
                m -= 1
            
            if i < m and arr[m] + arr[i] == 0:
                ret.add((arr[i], arr[m],))
            
        
        return sorted(ret)