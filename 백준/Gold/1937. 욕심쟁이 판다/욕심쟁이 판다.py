import sys
sys.setrecursionlimit(10**9)
def dfs(r, c):
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    visited[r][c] = 0  # 일단 현재 위치를 0으로 초기화
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        # 이동 가능한 경우 체크
        if 0 <= nr < N and 0 <= nc < N and board[r][c] < board[nr][nc] and visited[nr][nc] == -1:
            visited[nr][nc] = 0  # 이동 가능한 위치가 있다면 일단 이동 가능한 위치도 0으로 초기화
            dfs(nr, nc)  # 탐색이 끝나서 돌아왔으면 그 위치의 + 1 값을 체크

    # dfs탐색이 끝났으면 4개의 위치를 다시 탐색하면서 가장 많이 움직일 수 있는 칸 + 1을 현재 값에 넣어줌
    max_cnt = 0
    for d in range(4):
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < N and 0 <= nc < N and board[r][c] < board[nr][nc]:  # 갈 수 있는 칸들 중 가장 큰 값에 +1
            cnt = visited[nr][nc]
            max_cnt = max(max_cnt, cnt)
    visited[r][c] = max_cnt + 1

    return visited[r][c]


N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

# 1. 대나무가 현재 값보다 더 큰 곳만 이동이 가능하다
# 2. 최대한 많은 칸을 이동해야하므로 현재 최종 위치에 도달하기까지 현재 칸에서 몇 칸을 더 움직일 수 있는지를 체크해야한다
# 방법 : DFS를 수행하면서 이동 가능한 위치를 넣어주고 그 전 단계로 돌아올 때 'nr, nc중 가장 큰 값'을 델타탐색해서 그 값에 +1을 더해준다

# 행렬을 하나 더 만들어서 그 dfs를 돌 때 해당 칸에서 얼마만큼 이동할 수 있었는지 체크를 해주어야한다
visited = [[-1] * N for _ in range(N)]
max_cnt = 0
for i in range(N):  # 시작 위치는 고정되어있지 않으므로 전체를 돌면서 시작 위치를 체크해주어야 한다.
    for j in range(N):
        cnt = dfs(i, j)
        max_cnt = max(cnt, max_cnt)
print(max_cnt)

