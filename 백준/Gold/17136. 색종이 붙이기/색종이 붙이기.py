
board = [list(map(int, input().split())) for _ in range(10)]
p_lst = [0, 0, 0, 0, 0]
# 1. 색종이 5*5에서 1*1까지 가능한지 체크
visited = [[False] * 10 for _ in range(10)]
stack = []
for i in range(10):
    for j in range(10):
        if board[i][j] == 1 :
            stack.append((i, j))
min_ans = 26
def backtracking(level):
    global min_ans
    if level == len(stack):
        min_ans = min(sum(p_lst), min_ans)
        return
    r = stack[level][0]
    c = stack[level][1]
    if visited[r][c] == False :
        #색종이 사용 가능한 걸 모두 사용해보기
        for p in range(5, 0, -1):
            if p_lst[p-1] < 5 : #종이 사용 개수 확인
                check = True

                #사용 가능한 종이라면 종이 붙일 때 색종이가 겹치거나 0이 있는지 확인
                if not(0 <= r+(p-1) < 10 and 0 <= c + (p-1) < 10) :
                    continue

                for i in range(p):
                    for j in range(p):
                        if board[r+i][c+j] == 0 or visited[r+i][c+j] == True :
                            check = False
                            break
                if check : # 종이를 붙일 수 있다면 붙이고 다음으로 넘어가기
                    p_lst[p - 1] += 1
                    if sum(p_lst) > min_ans :
                        p_lst[p -1] -= 1
                        return
                    for i in range(p):
                        for j in range(p):
                            visited[r+i][c+j] = True
                    backtracking(level+1)
                    for i in range(p):
                        for j in range(p):
                            visited[r+i][c+j] = False
                    p_lst[p - 1] -= 1
    else : # 색종이가 이미 붙여져있다면 다음으로 넘어가기
        backtracking(level+1)

if stack :
    backtracking(0)
    if min_ans == 26 :
        print(-1)
    else :
        print(min_ans)
else :
    print(0)


