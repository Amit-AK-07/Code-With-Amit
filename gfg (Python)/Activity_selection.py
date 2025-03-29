class Solution:
    def activitySelection(self, start, finish):
        #code here
        n = len(start)
        activities = sorted(zip(start, finish), key=lambda x: x[1])
        count = 1
        last_finish = activities[0][1]
        
        for i in range(1, n):
            if activities[i][0] > last_finish:
                count += 1
                last_finish = activities[i][1]
        return count
        
