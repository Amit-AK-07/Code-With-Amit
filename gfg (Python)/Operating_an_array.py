# Your task is to complete all
# three functions

# if the element is found in the list
# function  must return true or else
# return false
class Solution:
    
    def searchEle(self,arr, x):
        # Code here
        for i in range(len(arr)):
            if arr[i] == x:
                return True
        return False
    
    # insert element if you have inserted properly 1 will be printed else 0
    def insertEle(self,arr, y, yi):
        # Code here
        if 0 <= yi <= len(arr):
            arr.insert(yi,y)
            return True
        return False
    
    # delete element if you have deleted properly 1 will be printed else 0
    def deleteEle(self,arr, z):
        # Code here
        if z in arr:
            arr.remove(z)
            return True
        return False
        