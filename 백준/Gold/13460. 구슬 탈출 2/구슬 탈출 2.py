def bfs():
    while q:
        rr, rc, br, bc, depth = q.popleft()
        if depth > 10 :
            return -1
        crr, crc, cbr, cbc = rr, rc, br, bc
        for d in range(4):
            if arr[rr+dr[d]][rc+dc[d]] != "#" or arr[br+dr[d]][bc+dc[d]] != "#" :
                crr, crc = move(rr, rc, br, bc, d)
                cbr, cbc = move(br, bc, crr, crc, d)
                crr, crc = move(crr, crc, cbr, cbc, d)

                if (cbr, cbc) == (-1, -1) :
                    continue
                elif (crr, crc) == (-1, -1):
                    return depth
                else :
                    q.append((crr, crc, cbr, cbc, depth+1))

def move(r, c, xr, xc, d):
    cr = r
    cc = c
    while 0 <= cr < N and 0 <= cc < M :
        nr = cr +dr[d]
        nc = cc + dc[d]
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != '#' and (nr, nc) != (xr, xc) :
            cr = nr
            cc = nc
        else :
            break

        if arr[cr][cc] == 'O' :
            return -1, -1
    return cr, cc

from collections import deque

N, M = map(int, input().split())

arr = [list(input()) for _ in range(N)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

for i in range(N):
    for j in range(M):
        if arr[i][j] == 'R' :
            rr, rc = i, j
        if arr[i][j] == 'B' :
            br, bc = i, j
q = deque()
q.append((rr, rc, br, bc, 1))
print(bfs())