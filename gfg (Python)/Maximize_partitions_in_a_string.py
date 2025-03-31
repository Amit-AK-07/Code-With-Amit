class Solution:
    def maxPartitions(self , s):
        # code here
        n = len(s)
        last_occurence = {}
        count = 0
        end = 0
        
        for i, char in enumerate(s):
            last_occurence[char] = i
            
        for i, char in enumerate(s):
            end = max(last_occurence[char], end)
            if i == end:
                count += 1
        return count
