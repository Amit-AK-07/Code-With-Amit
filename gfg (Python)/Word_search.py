class Solution:
    def isWordExist(self, mat, word):
        #Code here
        rows = len(mat)
        cols = len(mat[0])
        n = len(word)
        
        def dfs(i, j, index):
            if index == len(word):
                return True
            if i < 0 or i >= rows or j < 0 or j >= cols or mat[i][j] != word[index]:
                return False
            
            temp = mat[i][j]
            mat[i][j] = '#'
            
            found = (dfs(i + 1, j, index + 1) or 
                     dfs(i - 1, j, index + 1) or 
                     dfs(i, j + 1, index + 1) or 
                     dfs(i, j - 1, index + 1))
            
            mat[i][j] = temp 
            return found
        
        for i in range(rows):
            for j in range(cols):
                if mat[i][j] == word[0]:
                    if dfs(i, j, 0):
                        return True
        
        return False

