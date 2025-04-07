#User function Template for python3

class Solution:
    
    #Function to return a list containing the DFS traversal of the graph.
    def dfs(self, adj):
        # code here
        def dfs_traversal(node):
            seen.add(node)
            res.append(node)
            
            for i in adj[node]:
                if i not in seen:
                    dfs_traversal(i)
        
        seen, res = set(), []
        dfs_traversal(0)
        return res