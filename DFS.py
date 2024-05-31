def initiateDFSTraversal(node, visited, adj, result):
    result.append(node)
    visited[node] = True 
 
    for neighbour in adj[node]:
        if visited[neighbour] == False:
            initiateDFSTraversal(neighbour, visited, adj, result)
 
def printDFSTraversal(adj, n):
    visited = [False] * n 
    result = []
    for node in range(n):
        if visited[node] == False:
            initiateDFSTraversal(node, visited, adj, result)
 
    print("DFS traversal is: ", result)
 
 
# Adjacency List Construction 
n, m = map(int, input().split())
adj = [] 
for i in range(n):
    adj.append([])
 
for i in range(m):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
 
# printBFSTraversal(adj, n)
printDFSTraversal(adj, n)
