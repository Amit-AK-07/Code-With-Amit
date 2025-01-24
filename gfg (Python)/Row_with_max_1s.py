class Solution:
    def rowWithMax1s(self, arr):
        # code here
        for i in range(len(arr[0])):
            for j in range(len(arr)):
                if(arr[j][i] == 1):
                    return j
        return -1
