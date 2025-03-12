#Back-end complete function Template for Python 3

class Solution:
    def minCostClimbingStairs(self, cost):
        #Write your code here
        stair_case = stair = 0
        for i in cost:
            stair_case, stair = stair, min(stair_case, stair) + i
        return min(stair_case, stair)
