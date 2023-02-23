from collections import deque
def bfs(queue):
    global cnt

    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]
    while queue :
        r, c = queue.popleft()
        visited[r][c] = True
        if board[r][c] == 1 :
            cnt += 1
        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == False :
                visited[nr][nc] = True
                next_queue.append((nr, nc))


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]
    max_cnt = 0
    house = 0

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1 :
                house += 1
    for i in range(N):
        if max_cnt == house :
            break
        for j in range(N):
            queue = deque([(i, j)])
            next_queue =deque([])
            cnt = 0
            #k번 bfs 돌리기
            visited = [[False] * N for _ in range(N)]
            for k in range(N*2):
                bfs(queue)
                queue = next_queue
                next_queue = deque([])
                if cnt * M >= (k+1) * (k+1) + k * k :
                    max_cnt = max(cnt, max_cnt)
    print(f"#{tc}", max_cnt)