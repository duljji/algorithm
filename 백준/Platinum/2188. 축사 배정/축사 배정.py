'''
1
5 5
2 5
2 5
2 5
1 2
1 1
'''
def bimatch(graph, N, M, pair):
    pair.update((i, None) for i in range(1, M+1))

    def dfs(u, visit):
        for v in graph[u] : # i번째 소가 들어갈 수 있는 축사 탐색
            if not visit[v] : # 방문한 적이 없는 축사라면
                visit[v] = True # 축사 방문 처리 한 뒤
                if pair[v] is None or dfs(pair[v], visit): # 해당 축사에 소가 없거나 축사에 있는 소가 다른 곳에 방문이 가능하다면
                    pair[v] = u # 소를 해당 축사에 넣기
                    return True # 소를 축사에 넣었다고 반환하기
        return False # 소를 넣을 수 있던 적이 한번도 없다면 False

    match = 0
    for i in range(N):
        if dfs(i, [False] * (M+1)): # 소 하나 선택해서 들어갈 수 있는 N개의 축사 탐색하기
            match += 1

    return match


N, M = map(int, input().split())
adj = [[] for _ in range(N)]
for _ in range(N):
    a, *b = map(int, input().split())
    adj[_].extend(b)

print(bimatch(adj, N, M, dict()))
