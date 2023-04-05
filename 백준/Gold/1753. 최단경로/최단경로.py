import sys
input = sys.stdin.readline
def dijkstra(s, V):
    U = [0] * (V+1)
    D[s] = 0
    for e, w in adj[s] :
        D[e] = min(D[e], w)
    U[s] = 1
    for _ in range(V+1):
        minV = INF
        t = 0
        for i in range(V+1):
            if U[i] == 0 and minV > D[i] :
                minV = D[i]
                t = i
        U[t] = 1
        for e, w in adj[t] :
            D[e] = min(D[e], D[t]+w)


V, E = map(int, input().split())
S = int(input())
adj = [[] for _ in range(0, V+1)]
for _ in range(E):
    s, e, w = map(int, input().split())
    adj[s].append((e, w))
INF = 1000000000
D = [INF] * (V+1)
dijkstra(S, V)
for i in range(1, V+1):
    if D[i] == INF:
        print('INF')
    else :
        print(D[i])
