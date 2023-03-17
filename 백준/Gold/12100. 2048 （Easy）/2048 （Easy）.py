'''
3
2 4 8
2 4 8
2 4 8

3
4 8 16
8 4 2
4 8 16

3
2 2 2
2 2 2
2 2 2

3
2 4 8
4 8 2
8 4 2

4
2 2 4 16
0 0 0 0
0 0 0 0
0 0 0 0
'''
from copy import deepcopy

# 전 후 좌 우로 모두 이동 - 5번 해보면서 최댓값 찾기

def dfs(n, d, tmp_board):
    global max_ans
    visited = [[False] * N for _ in range(N)]
    if n == 5 :
        for r in tmp_board :
            max_ans = max(max_ans, max(r))
        return
    if d == 0: #0일경우 상단으로 모두 옮기기
        board = deepcopy(tmp_board)
        for j in range(N):
            for i in range(1, N):
                cr = i
                nr = cr + dr[d]
                while 0 <= nr < N and board[nr][j] == 0 :
                    board[nr][j], board[cr][j] = board[cr][j], board[nr][j]
                    cr = nr
                    nr = cr + dr[d]
                if 0 <= nr < N and board[nr][j] == board[cr][j] and visited[nr][j] == False:
                    visited[nr][j] = True
                    board[nr][j] += board[cr][j]
                    board[cr][j] = 0
    if d == 1:  # 1일경우 아래로 모두 옮기기
        board = deepcopy(tmp_board)
        for j in range(N):
            for i in range(N-2, -1, -1):
                cr = i
                nr = cr + dr[d]
                while 0 <= nr < N and board[nr][j] == 0:
                    board[nr][j], board[cr][j] = board[cr][j], board[nr][j]
                    cr = nr
                    nr = cr + dr[d]
                if 0 <= nr < N and board[nr][j] == board[cr][j] and visited[nr][j] == False:
                    visited[nr][j] = True
                    board[nr][j] += board[cr][j]
                    board[cr][j] = 0
    if d == 2 : #d가 2면 왼쪽으로 이동
        board = deepcopy(tmp_board)
        for i in range(N):
            for j in range(1, N):
                cc = j
                nc = cc + dc[d]
                while 0 <= nc < N and board[i][nc] == 0:
                    board[i][nc], board[i][cc] = board[i][cc], board[i][nc]
                    cc = nc
                    nc = cc + dc[d]
                if 0 <= nc < N and board[i][nc] == board[i][cc] and visited[i][nc] == False:
                    visited[i][nc] = True
                    board[i][nc] += board[i][cc]
                    board[i][cc] = 0
    if d == 3:  # d가 2면 왼쪽으로 이동
        board = deepcopy(tmp_board)
        for i in range(N):
            for j in range(N-2, -1, -1):
                cc = j
                nc = cc + dc[d]
                while 0 <= nc < N and board[i][nc] == 0:
                    board[i][nc], board[i][cc] = board[i][cc], board[i][nc]
                    cc = nc
                    nc = cc + dc[d]
                if 0 <= nc < N and board[i][nc] == board[i][cc] and visited[i][nc] == False:
                    board[i][nc] += board[i][cc]
                    visited[i][nc] = True
                    board[i][cc] = 0
    dfs(n+1, 0, board)
    dfs(n+1, 1, board)
    dfs(n+1, 2, board)
    dfs(n+1, 3, board)
N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
max_ans = 2
dfs(0, 0, board)
dfs(0, 1, board)
dfs(0, 2, board)
dfs(0, 3, board)
print(max_ans)