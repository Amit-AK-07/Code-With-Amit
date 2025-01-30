#User function Template for python3

class Solution:
    def transpose(self, mat, n):
        # Write Your code here
        for i in range(n):
            for j in range(i + 1, n):
                mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
