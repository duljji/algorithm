from collections import deque
N = int(input())

def is_valid(r, c):
    return 0 <= r < N and 0 <= c < N

def bfs():
    global cnt
    q = deque()
    q.append((0, 0))
    v = [[-1] * N for _ in range(N)]
    v[0][0] = arr[0][0]
    while q :
        r, c = q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if is_valid(nr, nc) :
                if v[nr][nc] == -1 :
                    v[nr][nc] = v[r][c] + arr[nr][nc]
                    q.append((nr, nc))
                else :
                    if v[nr][nc] > v[r][c] + arr[nr][nc] :
                        v[nr][nc] = v[r][c] + arr[nr][nc]
                        q.append((nr, nc))
    print(f"Problem {cnt}:",v[N-1][N-1])
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
cnt = 1
while N!=0 :

    arr = [list(map(int, input().split())) for _ in range(N)]
    bfs()
    N = int(input())
    cnt += 1