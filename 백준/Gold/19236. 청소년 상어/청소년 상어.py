from copy import deepcopy
def dfs(tmp_board, r, c, ans, depth):
    global max_ans
    board = deepcopy(tmp_board)
    # 2. shark 어항에 넣기
    ans += board[r][c][0]
    shark = [-1, board[r][c][1]]
    board[r][c] = shark

    # 3. 물고기 이동 및 상어 이동 가능 확인
    for f in range(1, 17):
        check = False
        for i in range(4):
            for j in range(4):
                if board[i][j][0] == f:  # f번 물고기부터 차례대로 이동 시작
                    for d in range(8):
                        nr = i + dr[(board[i][j][1] + d) % 8]
                        nc = j + dc[(board[i][j][1] + d) % 8]
                        if 0 <= nr < 4 and 0 <= nc < 4 and (nr, nc) != (r, c):
                            board[i][j][1] = (board[i][j][1]+d) % 8
                            board[i][j], board[nr][nc] = board[nr][nc], board[i][j]
                            check = True
                            break
                if check :
                    break
            if check:
                break

    #상어 다음 타겟 찾기
    board[r][c] = [0, 0] #현재 위치 비워두기
    cr, cc = r, c
    while 0 <= cr + dr[shark[1]] < 4 and 0 <= cc + dc[shark[1]] < 4 :
        nr = cr + dr[shark[1]]
        nc = cc + dc[shark[1]]
        if board[nr][nc][0] != 0 :
            dfs(board, nr, nc, ans, depth+1)
        cr = nr
        cc = nc
        
    #while 문이 끝났다면 이동 할 수 있는 경우를 모두 찾았다는 것
    max_ans = max(ans, max_ans)

# 1. 4x4 어항에 물고기 넣기
dr = [-1, -1, 0, 1, 1, 1, 0, -1]
dc = [0, -1, -1, -1, 0, 1, 1, 1]
f_lst = []
board = [[0] * 4 for _ in range(4)]
for i in range(4):
    flst = list(map(int, input().split()))
    for j in range(4):
        board[i][j] = [flst[j * 2], flst[j * 2 + 1] -1]
max_ans = 0
dfs(board, 0, 0, 0, 0)
print(max_ans)
