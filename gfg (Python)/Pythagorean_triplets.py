class Solution:
    from collections import Counter
    def pythagoreanTriplet(self, arr):
        # code here
        squareCount = Counter(x * x for x in arr)
        
        squares = list(squareCount.keys())
        
        for i in range(len(squares)):
            for j in range(i+1, len(squares)):
                sum_of_squares = squares[i] + squares[j]
                if sum_of_squares in squareCount:
                    return True
          
        return False