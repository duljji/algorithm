from collections import deque


def f_bfs():
    while f_q:
        r, c, depth = f_q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and f_visited[nr][nc] == False and board[nr][nc] != "#":
                f_visited[nr][nc] = True
                f_q.append((nr, nc, depth + 1))
        if f_q:
            if depth != f_q[0][2]:
                return


def s_bfs():
    while s_q:
        r, c, depth = s_q.popleft()
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < M and s_visited[nr][nc] == False and board[nr][nc] != "#" and f_visited[nr][
                nc] == False:
                s_visited[nr][nc] = True
                s_q.append((nr, nc, depth + 1))
            elif not (0 <= nr < N and 0 <= nc < M):
                return depth+1

        if s_q:
            if depth != s_q[0][2]:
                return 0
        else:
            return 0


T = int(input())
for tc in range(1, T + 1):
    M, N = map(int, input().split())

    board = [list(input()) for _ in range(N)]

    f_q = deque()
    s_q = deque()
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    f_visited = [[False] * M for _ in range(N)]
    s_visited = [[False] * M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if board[i][j] == "*":
                f_q.append((i, j, 0))
                f_visited[i][j] = True
            elif board[i][j] == "@":
                s_q.append((i, j, 0))
                s_visited[i][j] = True
    check = 0
    while True:
        f_bfs()
        check = s_bfs()
        if check != 0:
            print(check)
            break
        elif not s_q:
            print("IMPOSSIBLE")
            break
