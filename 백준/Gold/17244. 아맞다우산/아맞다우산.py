'''
5 5
#####
#####
#SXX#
..XXX
####E
'''
from collections import deque


def is_valid(r, c):
    return 0 <= r < R and 0 <= c < C


def bfs():
    key = 0
    depth = 0
    q = deque()
    q.append((si, sj, key, depth))
    v = [[-1] * C for _ in range(R)]
    v[si][sj]=0
    while q:
        r, c, key, depth = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc) and arr[nr][nc] != '#' :
                if v[nr][nc] & key != key or v[nr][nc] == -1 :
                    v[nr][nc] = key
                    if arr[nr][nc] == 'E' :
                        if key == ans :
                            return depth+1
                    elif  'a' <= arr[nr][nc] <= 'e' :


                        v[nr][nc] = key
                        q.append((nr, nc, key | 1 << ord(arr[nr][nc]) - ord('a'), depth+1))
                    else:
                        q.append((nr, nc, key, depth+1))


C, R = map(int, input().split())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
arr = [list(input()) for _ in range(R)]
si = sj = 0  # 시작 위치
X = 0
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'S':
            si, sj = i, j
            arr[i][j] = '.'
        elif arr[i][j] == 'X':
            arr[i][j] = chr(ord('a')+X)
            X += 1
ans = 0
for i in range(X):
    ans += 1 << i
print(bfs())


