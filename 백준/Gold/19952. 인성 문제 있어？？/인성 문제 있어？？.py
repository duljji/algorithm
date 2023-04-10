from pprint import pprint
from collections import deque


def is_valid(r, c):
    return 0 <= r < R and 0 <= c < C


def bfs():
    q = deque()
    q.append((si, sj))
    v = [[-1] * C for _ in range(R)]
    v[si][sj] = F
    while q:
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc):
                # 1. 장애물이 있다면 이동 가능한지 먼저 파악해야함
                if arr[nr][nc] - arr[r][c] <= v[r][c] : # 뛰어넘어야 할 장애물의 높이가 현재 가지고있는 힘보다 작다면
                    if v[nr][nc] == -1 and v[r][c] != 0:
                        v[nr][nc] = v[r][c] - 1
                        q.append((nr, nc))
                    elif v[nr][nc] < v[r][c] - 1 :
                        v[nr][nc] = v[r][c] - 1
                        q.append((nr, nc))

    if v[ei][ej] != -1 :
        print("잘했어!!")
    else :
        print("인성 문제있어??")


T = int(input())

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
for tc in range(1, T + 1):
    R, C, N, F, si, sj, ei, ej = map(int, input().split())
    si -= 1
    sj -= 1
    ei -= 1
    ej -= 1
    arr = [[0] * C for _ in range(R)]

    for i in range(N):
        r, c, h = map(int, input().split())
        arr[r - 1][c - 1] = h
    bfs()

