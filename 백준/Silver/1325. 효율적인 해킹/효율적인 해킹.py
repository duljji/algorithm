from collections import deque


def bfs(start) :
    i = start
    queue = deque([i])
    visited = [0] * (V+1)
    cnt = 0
    visited[i] = True
    while queue :
        n = queue.popleft()

        for j in adj[n] :
            if visited[j] == False :
                visited[j] = True
                queue.append(j)
                cnt += 1
    cnt_lst.append(cnt)

V, E = map(int, input().split())

adj = [[] for _ in range(V+1)]
for i in range(E):
    s, e = map(int, input().split())
    adj[e].append(s)
cnt_lst = []
for i in range(1, V+1):
    bfs(i)
max_v = max(cnt_lst)
for i in range(len(cnt_lst)):
    if cnt_lst[i] == max_v :
        print(i+1, end=" ")