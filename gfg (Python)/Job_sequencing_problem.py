class Solution:
    def jobSequencing(self, deadline, profit):
        # code here
        n = len(deadline)
        jobs = list(zip(deadline, profit))
        # Sort jobs by profit in descending order
        jobs.sort(key=lambda x: -x[1])
        
        max_deadline = max(deadline) if deadline else 0
        parent = [i for i in range(max_deadline + 1)]
        
        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u
        
        def union(u, v):
            parent[v] = u
        
        count = 0
        total_profit = 0
        
        for d, p in jobs:
            available_slot = find(d)
            if available_slot > 0:
                count += 1
                total_profit += p
                union(find(available_slot - 1), available_slot)
        
        return [count, total_profit]
