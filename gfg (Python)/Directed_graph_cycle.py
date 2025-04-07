class Solution:
    def isCycle(self, V, edges):
        # code here
        from collections import defaultdict

    # Build the adjacency list
        adj = defaultdict(list)
        for u, v in edges:
            adj[u].append(v)
    
        visited = [False] * V
        rec_stack = [False] * V
    
        def is_cyclic_util(node):
            visited[node] = True
            rec_stack[node] = True
    
            for neighbor in adj[node]:
                if not visited[neighbor]:
                    if is_cyclic_util(neighbor):
                        return True
                elif rec_stack[neighbor]:
                    return True
    
            rec_stack[node] = False
            return False
    
        for node in range(V):
            if not visited[node]:
                if is_cyclic_util(node):
                    return True
    
        return False
