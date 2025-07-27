class Solution:
    def findMajority(self, arr):
        # code here
        ans = []
        freq = {}
        
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
            
            
        for num, count in freq.items():
            if count > len(arr) // 3:
                ans.append(num)
                
        ans.sort()
        
        return ans
            