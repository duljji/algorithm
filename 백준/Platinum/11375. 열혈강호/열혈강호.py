def bimatch(graph, N, M, pair) :
    pair.update((i, None) for i in range(1, M+1))

    def dfs(u, visited):
        stack = [u]
        while stack:
            u = stack.pop()
            for v in graph[u]:
                if not visited[v]:
                    visited[v] = True
                    if pair[v] is None:
                        pair[v] = u
                        return True
                    elif pair[v] != u:
                        stack.append(pair[v])
                        pair[v] = u
        return False

    match = 0
    for i in range(N):
        if dfs(i, [False] * (M+1)):
            match += 1

    return match


N, M = map(int, input().split())

adj = [[] for _ in range(N)]

for n in range(N):
    a, *b = map(int, input().split())
    adj[n].extend(b)
print(bimatch(adj, N, M, dict()))
