from pprint import pprint
from collections import deque

def is_valid(r, c):
    return 0 <= r < N and 0 <= c < M
def bfs():
    global ans, ans2
    q = deque()
    q.append((0, 0, False))
    while q :
        r, c, flag = q.popleft()
        if r == N-1 and c == M-1 and flag :
            ans2 += 1
        if arr[r][c] == 1 :
            flag = True
        for d in range(2):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc) :
                q.append((nr, nc, flag))



dr = [1, 0]
dc = [0, 1]
N, M, K =map(int, input().split())
ans = 0
ans2 = 0
arr = [[0] * M for _ in range(N)]

tr, tc = K//M, K%M

arr[tr][tc] = 1
bfs()
print(ans2)