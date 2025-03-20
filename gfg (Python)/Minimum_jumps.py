class Solution:
    def minJumps(self, arr):
        # code here
        count = 0
        curr = 0
        far = 0

        if len(arr) > 1 and arr[0] == 0:
            return -1

        for i in range(len(arr) - 1):
            # Update the farthest point that can be reached
            far = max(far, arr[i] + i)
            
             # If the current position matches the farthest reached position
            if i == curr:
               
                curr = far
                count += 1
                # If the farthest point is less than or equal to the current index, return -1 (unreachable)
                if curr <= i:
                    return -1

        return count
        