from pprint import pprint
def move(r, c):
    cr, cc = r, c
    while cr != R :
        if board[cr][cc] == 0 :
            cr += 1
        elif board[cr][cc] == 1 :
            cr += 1
            cc += 1
        elif board[cr][cc] == -1 :
            cr += 1
            cc -= 1
    if cc == c :
        return True
    else :
        return False



 # 1. 현재 추가한 가로선으로 인해 모두가 자기 자리에 도착할 수 있는지 체크
def dfs(n):
    global min_n
    for c in range(C):
        if not move(0, c):
            break
    else:
        min_n = min(min_n, n)
        return

    if n == 3:
        return
    else :
        for i in range(R):
            for j in range(C-1):
                if board[i][j] == board[i][j+1] == 0 :
                    board[i][j] = 1
                    board[i][j+1] = -1
                    dfs(n+1)
                    board[i][j] = 0
                    board[i][j+1] = 0
    return


C, M ,R = map(int, input().split())
board = [[0] * C for _ in range(R+1)]
for _ in range(M):
    a, b = map(int, input().split())
    board[a-1][b-1] = 1
    board[a-1][b] = -1
min_n = 4
dfs(0)
if min_n == 4 :
    print(-1)
else :
    print(min_n)
