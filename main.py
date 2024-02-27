class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, dest: int) -> bool:
        if source == dest:
            return True
        
        # Build the graph using an adjacency list
        graph = defaultdict(list)
        
        for a,b in edges:
            graph[a].append(b)
            graph[b].append(a)  # Assuming it's an undirected graph, add both ways

        marked = [False] * n
       
        
        
        ## Using Recursive
        # def dfs(v):
        #     if v == dest:
        #         return True
        #     marked[v] = True
        #     for neighbor in graph[v]:
        #         if not marked[neighbor]:
        #             if dfs(neighbor):
        #                 return True
        #     return False        
        # return dfs(source)
                       
        ## Using Stack

        stack = [source]

        # Use a set for visited to optimize the lookup time
        visited = set()
        
        while stack:
            v = stack.pop()
            if v == dest:
                return True
            
            if v not in visited:
                visited.add(v)

            for neighbor in graph[v]:
                if neighbor not in visited:
                    stack.append(neighbor)
        return False              


        
