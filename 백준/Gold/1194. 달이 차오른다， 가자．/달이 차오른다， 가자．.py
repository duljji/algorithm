from collections import deque
import sys



def bfs():
    q = deque()
    q.append((si, sj, 0, 0))
    v = [[-1] * M for _ in range(N)]
    while q:
        r, c, keys, cnt = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != '#':
                # 갈 수 있는 위치지만 해당 위치에 현재 열쇠 상태로 가본 적이 있는지 확인
                if v[nr][nc] == -1 or (keys & v[nr][nc] != keys and keys != 0):
                    v[nr][nc] = keys
                    if arr[nr][nc] == '1':
                        return cnt + 1
                    elif 'a' <= arr[nr][nc] <= 'f':
                        q.append((nr, nc, keys | (1 << ord(arr[nr][nc]) - 97), cnt + 1))
                        v[nr][nc] = keys | (1 << ord(arr[nr][nc]) - 97)
                    elif 'A' <= arr[nr][nc] <= 'F':
                        door = ord(str.lower(arr[nr][nc])) - 97
                        if keys & (1 << door):
                            q.append((nr, nc, keys, cnt + 1))
                    else:
                        v[nr][nc] = keys
                        q.append((nr, nc, keys, cnt + 1))

    return -1


N, M = map(int, input().split())
arr = [input() for _ in range(N)]

for i in range(N):
    for j in range(M):
        if arr[i][j] == '0':
            si, sj = i, j

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
print(bfs())
