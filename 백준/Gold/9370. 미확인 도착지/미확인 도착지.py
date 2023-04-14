'''
1
5 5 2
1 2 3
1 4 3
4 5 3
1 2 2
2 3 2
3 5 2
3
5
3

Process finished with exit code 0


'''
import heapq
tc = int(input())
INF = 10**8
def dijkstra(start):
    distances = [[INF, []] for _ in range (N+1)]
    distances[start][0] = 0
    distances[start][1].append(start)
    q = [(0, start)]
    while q :
        current_distance, current_node = heapq.heappop(q)
        if distances[current_node][0] > current_distance :
            continue
        for neighbor, weight in adj[current_node] :
            distance = current_distance + weight
            if distances[neighbor][0] > distance :
                distances[neighbor][0] = distance
                distances[neighbor][1] = (distances[current_node][1] + [neighbor])[:]
                heapq.heappush(q, (distance, neighbor))
            elif distances[neighbor][0] == distance :
                d_lst = (distances[current_node][1] + [neighbor])[:]
                if G in d_lst and H in d_lst and abs(d_lst.index(G) - d_lst.index(H)) == 1 :
                    distances[neighbor][1] = d_lst


    for target in tlst :
        if G in distances[target][1] and H in distances[target][1] :
            if abs(distances[target][1].index(G) - distances[target][1].index(H)) == 1 :
                ans.append(target)


for t in range(1, tc + 1):
    N, M, T = map(int, input().split())
    S, G, H = map(int, input().split())
    adj = [[] for _ in range(N+1)]
    for _ in range(M):
        s, e, w = map(int, input().split())
        adj[s].append((e, w))
        adj[e].append((s, w))
    tlst =[]
    for _ in range(T):
        target = int(input())
        tlst.append(target)
    ans = []
    dijkstra(S)
    print(*sorted(ans))
