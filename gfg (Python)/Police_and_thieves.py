class Solution:
    def catchThieves(self, arr, k):
        #code  here
        n = len(arr)
        police = []
        thief = []
        caught = 0
        
        for i in range(n):
            if arr[i] == 'P':
                police.append(i)
            elif arr[i] == 'T':
                thief.append(i)
                
        i = j = 0
        
        while i < len(police) and j < len(thief):
            if abs(police[i] - thief[j]) <= k:
                caught += 1
                i += 1
                j += 1
            
            elif police[i] < thief[j]:
                i += 1
            else:
                j += 1
                
        return caught