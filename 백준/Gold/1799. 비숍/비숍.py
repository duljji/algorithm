from pprint import pprint


def dfs(k, cnt):
    global ans
    if ans >= cnt + (2 * N - k)//2:
        return

    if k >= 2 * N - 1:
        ans = max(ans, cnt)
        return

    else:
        for r, c in plst[k]:
            if v[r - c]:
                v[r - c] = False
                dfs(k + 2, cnt + 1)
                v[r - c] = True
        dfs(k + 2, cnt)


N = int(input())

arr = [list(map(int, input().split())) for _ in range(N)]
plst = [[] for _ in range(2 * N)]

# arr을 돌면서 넣을 수 1이 아니면 해당 백트래킹을 돌릴 수 있도록 리스트에 넣어주기
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            plst[i + j].append((i, j))
# 각 lst에 비숍을 넣을 수 있을지 없을지 체크하기 위한 v 리스트도 있어야함
v = [True] * (2 * N)
ans = 0
dfs(0, 0)
t = ans
ans = 0
dfs(1, 0)
t += ans
print(t)
