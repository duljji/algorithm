import sys
from collections import deque
sys.stdin = open("input.txt")
T = int(input())
for tc in range(1, T+1) :
    #세로 크기, 가로 크기, 시작지점의 세로, 가로좌표, 탈출 후 소요된 시간 L

    R, C, sR, sC, L = map(int, input().split())

    board =[list(map(int, input().split())) for _ in range(R)]
    #이동 가능한 경우
    # 1 - 상 하 좌우 , 2 - 상하, 3 - 좌우, 4 - 상우, 5 - 하우, 6 - 하좌, 7 - 상좌
    # 상으로 갈 경우 하가 뚫려있는 1, 2, 5, 6 가능
    # 하로 갈 경우 상이 뚫려있는 1, 2, 4, 7 가능
    # 좌로 갈경우 우가 뚫려있는 1, 3, 4, 5 가능
    # 우로 갈 경우 좌가 뚫려있는 1, 3, 6, 7 가능
    dr = [-1, 1, 0, 0]
    dc = [0, 0, -1, 1]

    def is_valid(r, c, d):
        if 0 <= r < R and 0 <= c < C :
            check = board[r][c]
            if d == 0 :
                return check in [1, 2, 5, 6]
            elif d == 1 :
                return check in [1, 2, 4, 7]
            elif d == 2 :
                return check in [1, 3, 4, 5]
            elif d == 3 :
                return check in [1, 3, 6, 7]
            else :
                return False
        else :
            return False

    def is_valid2(r, c, d):
        if 0 <= r < R and 0 <= c < C :
            check = board[r][c]
            if d == 0 :
                return check in [1, 2, 4, 7]
            elif d == 1 :
                return check in [1, 2, 5, 6]
            elif d == 2 :
                return check in [1, 3, 6, 7]
            elif d == 3 :
                return check in [1, 3, 4, 5]
            else :
                return False
        else :
            return False

    def bfs(r, c, L):
        global cnt
        visited = [[0] * C for _ in range(R)]
        visited[r][c] = 1
        cnt += 1
        queue = deque([])
        queue.append((r, c))
        move_lst = []
        while queue :
            r, c = queue.popleft()
            if visited[r][c] == L :
                return

            for d in range(4):
                nr = r + dr[d]
                nc = c + dc[d]
                print(is_valid2(r, c, d))
                if is_valid2(r, c, d) and is_valid(nr, nc, d) and visited[nr][nc] == 0  :
                    cnt += 1
                    visited[nr][nc] = visited[r][c] + 1
                    queue.append((nr, nc))

    cnt = 0
    bfs(sR, sC, L)
    print(f"#{tc}", cnt)
