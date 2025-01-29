#User function Template for python3
import datetime

class Solution:
    def getDayOfWeek(self, d, m, y):
        # code here 
        day = datetime.date(y,m,d)
        p = day.weekday()
        
        if(p == 0):
            return "Monday"
        
        if(p == 1):
            return "Tuesday"
            
        if(p == 2):
            return "Wednesday"
            
        if(p == 3):
            return "Thursday"
            
        if(p == 4):
            return "Friday"
            
        if(p == 5):
            return "Saturday"
            
        if(p == 6):
            return "Sunday"
