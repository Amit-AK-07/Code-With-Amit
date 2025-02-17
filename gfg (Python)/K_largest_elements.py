class Solution:
    def kLargest(self, arr, k):
        # Your code here
        ans = []
        arr.sort(reverse = True)
        
        for i in range(k):
            ans.append(arr[i])
            
        return ans
