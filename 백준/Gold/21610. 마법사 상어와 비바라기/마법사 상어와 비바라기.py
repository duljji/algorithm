from pprint import pprint

N, M = map(int, input().split())

arr = [list(map(int, input().split())) for _ in range(N)]
lst = []
for _ in range(M):
    a, b = map(int, input().split())
    lst.append((a, b))

# 1. 구름 고르기 (N,1) (N,2), (N-1,1), (N-1,2)
cloud = [(N - 1, 0), (N - 1, 1), (N - 2, 0), (N - 2, 1)]
ans = 0
# 인덱스이므로 -1 해주기
for m in range(M):
    next_lst = []
    v = [[False] * N for _ in range(N)]
    # 2. 구름 이동하기
    dr = [0, 0, -1, -1, -1, 0, 1, 1, 1]
    dc = [0, -1, -1, 0, 1, 1, 1, 0, -1]
    d, cnt = lst[m]  # 이동방향과 횟수 체크

    while cloud:
        r, c = cloud.pop()
        nr = r + dr[d] * (cnt % N)
        nc = c + dc[d] * (cnt % N)

        # 만약 0 을 뚫거나 N-1을 뚫었다면 다시 맵 안으로 들어오게 처리해주기
        if nr < 0:
            nr += N
        elif nr >= N:
            nr -= N
        if nc < 0:
            nc += N
        elif nc >= N:
            nc -= N
        arr[nr][nc] += 1
        v[nr][nc] = True
        next_lst.append((nr, nc))


    while next_lst:  # 이번엔 대각선에 0이 아닌 값이 존재하는지 탐색 (방향 1, 3, 5, 7)
        r, c = next_lst.pop()
        for d in (2, 4, 6, 8):
            nr = r + dr[d]
            nc = c + dc[d]
            if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != 0:
                arr[r][c] += 1
    for i in range(N):
        for j in range(N):
            if arr[i][j] >= 2 and not v[i][j]:
                cloud.append((i, j))
                arr[i][j] -= 2
for i in range(N):
    for j in range(N):
        ans += arr[i][j]
print(ans)

