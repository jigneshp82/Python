graph = [[1,2,3],[0,2],[0,1,3],[0,2,5], [5],[2,4]]
visited = []
"""
start with first node - 0
check if node is in visited list:
    if not then add and start dfs on that node
    if already visisted then do nothing

"""

def dfs(graph,visited,node):
    if node not in visited:
        visited.append(node)
        print (node)
        for n in graph[node]:
            dfs(graph,visited,n)


dfs(graph, visited, 0)