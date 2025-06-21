import heapq
class Solution:
    def printKClosest(self, arr, k, x):
        # code here
        ans = []
        
        for i in arr:
            if i != x:
                heapq.heappush(ans,(abs(i - x), -i))
        
        r = []
        while ans and k > 0:
            _,i = heapq.heappop(ans)
            r.append(-i)
            k -= 1
        return r