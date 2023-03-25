from collections import deque


def dfs(n, g_cnt, r_cnt, v):
    global ans
    if n == len(p_lst):
        if g_cnt == G and r_cnt == R:
            r_q = deque()
            g_q = deque()
            for i in range(len(v)):
                if v[i] == 1:
                    g_q.append(p_lst[i]+[0])
                elif v[i] == 2:
                    r_q.append(p_lst[i]+[0])
            ans = max(ans, bfs(g_q, r_q))
    else:
        if g_cnt < G:
            v[n] = 1
            dfs(n + 1, g_cnt + 1, r_cnt, v)
            v[n] = 0
        if r_cnt < R:
            v[n] = 2
            dfs(n + 1, g_cnt, r_cnt + 1, v)
            v[n] = 0

        dfs(n + 1, g_cnt, r_cnt, v)


def bfs(g_q, r_q):
    next_g_q = deque()
    next_r_q = deque()
    vv = [[(0, 0)] * M for _ in range(N)]
    cnt = 0
    for r, c, depth in g_q :
        vv[r][c] = [1, depth]
    for r, c, depth in r_q :
        vv[r][c] = [2, depth]
    while True :
        while g_q:
            r, c, depth = g_q.popleft()
            if vv[r][c][0] == 3 :
                continue
            for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 0:
                    if vv[nr][nc][0] == 1 or vv[nr][nc][0] == 3:  # 초록색이 심겨져있는 곳, 꽃이 핀 곳이면 갈 필요 없음
                        continue
                    elif vv[nr][nc][0] == 2 : # 빨간색이 심겨져있는 곳이라면 꽃 개수 증가
                        if vv[nr][nc][1] == depth+1 :
                            vv[nr][nc] = (3, depth+1)
                            cnt += 1
                    else :
                        vv[nr][nc] = (1, depth+1)
                        next_g_q.append((nr, nc, depth+1))
        while r_q:
            r, c, depth = r_q.popleft()
            if vv[r][c][0] == 3 :
                continue
            for dr, dc in ((1, 0), (0, 1), (-1, 0), (0, -1)):
                nr = r + dr
                nc = c + dc
                if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] != 0:
                    if vv[nr][nc][0] == 2 or vv[nr][nc][0] == 3:  # 초록색이 심겨져있는 곳이면 갈 필요 없음
                        continue
                    elif vv[nr][nc][0] == 1 : # 빨간색이 심겨져있는 곳이라면 꽃 개수 증가
                        if vv[nr][nc][1] == depth+1 :
                            vv[nr][nc] = (3, depth+1)
                            cnt += 1
                    else :
                        vv[nr][nc] = (2, depth+1)
                        next_r_q.append((nr, nc, depth+1))

        if not next_r_q and not next_g_q :
            break
        else :
            r_q = next_r_q
            g_q = next_g_q
            next_r_q = deque()
            next_g_q = deque()

    return cnt

N, M, G, R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]

p_lst = []  # 배양액을 뿌릴 수 있는 땅

for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            p_lst.append([i, j])
v = [0] * len(p_lst)

# 배양액 뿌릴 수 있는 리스트를 백트래킹 하면서 G, R, X를 체크
ans = 0
dfs(0, 0, 0, v)
print(ans)