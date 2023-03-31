import sys
from collections import deque
N = int(input())
input = sys.stdin.readline
arr = [list(input().rstrip()) for _ in range(N)]
num_arr = [list(map(int, input().split())) for _ in range(N)]
si, sj = 0, 0
post = 0
num_lst = set()
maxv = 0
for i in range(N):
    for j in range(N):
        if arr[i][j] == 'P' :
            maxv = max(maxv, num_arr[i][j])
            si, sj = i, j
        elif arr[i][j] == 'K' :
            maxv = max(maxv, num_arr[i][j])
            post += 1
        num_lst.add(num_arr[i][j])
num_lst = sorted(num_lst)
left, right = 0, num_lst.index(maxv)
ans = 10**9
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]
while left < len(num_lst) and right < len(num_lst) :
    v = [[False] * N for _ in range(N)]
    q = deque()
    q.append((si, sj))
    k = 0
    if num_lst[left] <= num_arr[si][sj] <= num_lst[right] :
        while q :
            r, c = q.popleft()
            for d in range(8):
                nr = r + dr[d]
                nc = c + dc[d]
                if 0 <= nr < N and 0 <= nc < N :
                    if v[nr][nc] :
                        continue
                    elif num_lst[left] <= num_arr[nr][nc] <= num_lst[right] :
                        v[nr][nc] = True
                        q.append((nr, nc))
                        if arr[nr][nc] == 'K' :
                            k += 1
                else :
                    continue
    if k == post :
        ans = min(ans, num_lst[right] - num_lst[left])
        left += 1
    elif right < len(num_lst):
        right += 1
    else :
        break

print(ans)


