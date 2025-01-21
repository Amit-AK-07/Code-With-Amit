
class Solution:
    def findDuplicates(self, arr):
        # code here
        n = len(arr)
        arr.sort()
        ans = []
                
        for i in range(0, n - 1):
            if (arr[i] == arr[i + 1]):
                ans.append(arr[i])
        ans = list(dict.fromkeys(ans))
        return ans
        

