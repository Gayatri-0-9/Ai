graph={}
n=int(input('Enter the no of edges:'))
print('Enter the edges(eg: A B): ')
for _ in range (n):
    edge=input('Edge: ')
    u=edge[0]
    v=edge[2]
    
    if u not in graph:
        graph[u]=[]
    if v not in graph:
        graph[v]=[]
        
    graph[u].append(v)
    graph[v].append(u)
    
print(graph)

def dfs(node,visited):
    if node not in visited:
        print(node)
        visited.append(node)
        for neighbor in graph[node]:
            dfs(neighbor,visited)
            
def bfs(queue,visited):
    if len(queue)==0:
        return
    node=queue.pop(0)
    if node not in visited:
        print(node)
        visited.append(node)
        for neighbor in graph[node]:
            if neighbor not in visited and neighbor not in queue:
                queue.append(neighbor)
    bfs(queue,visited)
            
start=input('Enter the starting node:')
print('DFS:')
dfs(start,[])
print('BFS:')
bfs([start],[])