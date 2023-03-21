from collections import deque
def dfs(n, cnt, scnt):
    global ans
    if cnt > 7:
        return
    if n == 25 :
        if cnt ==7 and scnt>=4 :
            if check():
                ans += 1
        return
    v[n//5][n%5] = 1
    dfs(n + 1, cnt + 1, scnt + int(arr[n//5][n%5] == 'S'))
    v[n//5][n%5] = 0
    dfs(n + 1, cnt, scnt)

def check():
    for i in range(5):
        for j in range(5):
            if v[i][j] == 1 :
                return bfs(i, j)

def bfs(i, j):
    vv = [[0] * 5 for _ in range(5)]
    q = deque()
    q.append((i, j))
    vv[i][j] = 1
    cnt = 1
    while q :
        r, c = q.popleft()
        for nr, nc in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            if 0 <= r+nr < 5 and 0 <= c+nc < 5 and vv[r+nr][c+nc] == 0 and v[r+nr][c+nc] == 1 :
                q.append((r+nr, c+nc))
                vv[r+nr][c+nc] = 1
                cnt += 1
    return cnt==7


arr = [list(input()) for _ in range(5)]
v = [[0] * 5 for _ in range(5)]
ans = 0
dfs(0, 0, 0)
print(ans)