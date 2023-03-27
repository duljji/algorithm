from collections import deque

def is_valid(r, c):
    return 0 <= r < N and 0 <= c < M

def bfs(rr, rc, br, bc, depth):
    q = deque([(rr, rc, br, bc, depth)])
    visited = []
    while q :
        rr, rc, br, bc, depth = q.popleft()
        if depth > 10 :
            return False
        for d in range(4):
            crr = rr
            crc = rc
            cbr = br
            cbc = bc
            nrr = rr + dr[d]
            nrc = rc + dc[d]
            nbr = br + dr[d]
            nbc = bc + dc[d]
            r_check = False
            b_check = False
            while True :
                if is_valid(nrr, nrc) and board[nrr][nrc] != "#" and (nrr != cbr or nrc != cbc) :
                    crr = nrr
                    crc = nrc
                    nrr += dr[d]
                    nrc += dc[d]
                if board[crr][crc] == "O" :
                    r_check = True
                    crr = -1
                    crc = -1
                if is_valid(nbr, nbc) and board[nbr][nbc] != "#" and (nbr != crr or nbc != crc):
                    cbr = nbr
                    cbc = nbc
                    nbr += dr[d]
                    nbc += dc[d]
                if board[cbr][cbc] == "O" :
                    b_check = True
                    cbr = -1
                    cbc = -1
                    break
                if board[nrr][nrc] =="#" and board[nbr][nbc] == "#" :
                    break
                if board[nrr][nrc] == "#" and nbr == crr and nbc == crc :
                    break
                if board[nbr][nbc] == "#" and nrr == cbr and nrc == cbc :
                    break

                if crr == -1 and board[nbr][nbc] == "#" :
                    break
                if cbr == -1 :
                    break


            if not b_check and r_check :
                return depth
            if not b_check and (crr, crc, cbr, cbc) not in visited:
                visited.append((crr, crc, cbr, cbc))
                q.append((crr, crc, cbr, cbc, depth+1))

    return False




# 1. R과 B를 모두 q에 넣고 움직일 수 있는 경우 모두 움직이기

N, M = map(int, input().split())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
board = [list(input()) for _ in range(N)]

#R이 이동할 수 있는 경우를 모두 찾아서 돌려보기

for i in range(N):
    for j in range(M):
        if board[i][j] == "R" :
            board[i][j] = "."
            rr, rc = i, j
        if board[i][j] == "B" :
            board[i][j] = "."
            br, bc = i, j

if bfs(rr, rc, br, bc, 1) :
    print(1)
else :
    print(0)

