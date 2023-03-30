from pprint import pprint
import sys
def dfs(r, c):
    # r행 0열부터 시작
    v
    global ans
    if c == M-1 :
        ans += 1
        return True
    else :
        # 오른쪽 위로 갈 수 있는 경우
        check = True
        if 0 <= r - 1 < N and v[r-1][c+1] == False and arr[r-1][c+1] == '.':
            v[r-1][c+1] = True
            if dfs(r-1, c+1) :
                check = False

        # 오른쪽으로 갈 수 있는 경우
        if check and v[r][c+1] == False and arr[r][c+1] == '.':
            v[r][c+1] = True
            if dfs(r, c+1) :
                check = False


        # 오른쪽 아래로 갈 수 있는 경우
        if check and 0 <= r + 1 < N and v[r+1][c+1] == False and arr[r+1][c+1] == '.' :
            v[r+1][c+1] = True
            if dfs(r+1, c+1) :
                check = False


        if check :
            return False
        else :
            return True





input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(input()) for _ in range(N)]
v = [[False] * M for _ in range(N)]
ans = 0
for i in range(N):
    v[i][0] = True
    dfs(i, 0)

print(ans)