import sys
def dfs(graph, start):
    parent_children = {}
    stack = [start]
    
    while stack:
        n = stack.pop()
        
        if visited[n] == False:
            visited[n] = True
            for i in graph[n]:
                if visited[i] == False:
                    parent_children[i] = n
                    stack.append(i)
    return parent_children


input = sys.stdin.readline


N = int(input())
visited = [False] * (N + 1)
graph = {i: [] for i in range(1, N + 1)}
for _ in range(N - 1):
    A, B = map(int, input().split())
    graph[A].append(B)
    graph[B].append(A)

print_dic = dfs(graph, 1)
for i in range(2, N+1):
    print(print_dic[i])
