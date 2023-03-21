N, M, R = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
I = min(N, M)
v = [[0] * M for _ in range(N)]
for i in range(I // 2):
    lst = []

    for n in range(i, N - i):
        lst.append(arr[n][i])

    for n in range(i + 1, M - i):
        lst.append(arr[N - i - 1][n])

    for n in range(N - i - 2, i - 1, -1):
        lst.append(arr[n][M - i - 1])

    for n in range(M - i - 2, i, -1):
        lst.append(arr[i][n])

    r = R % len(lst)
    tmp_lst = [0] * len(lst)
    for j in range(len(lst)):
        idx = (j + r) % len(lst)
        tmp_lst[idx] = lst[j]
    d = 0
    sr, sc = i-1, i
    cnt = 0
    while d != 4:
        nr = sr + dr[d]
        nc = sc + dc[d]
        if 0 <= nr < N and 0 <= nc < M and v[nr][nc] == 0:
            v[nr][nc] = tmp_lst[cnt]
            sr = nr
            sc = nc
            cnt += 1
        else :
            d += 1
for ans in v:
    print(*ans)