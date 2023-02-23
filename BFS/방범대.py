import sys
sys.stdin = open('input.txt')
d = [0] * 21


# 운영 비용
def f(n):
    if n == 0:
        return 0
    elif n > 0:
        return n * n + (n - 1) * (n - 1)


T = int(input())
for tc in range(1, T + 1):
    # 영역의 크기에 따른 집의 수 저장
    r = [0] * 11
    N, M = map(int, input().split())
    lst = [list(map(int, input().split())) for _ in range(N)]
    # 집이 존재하는 좌표 담아
    home = []
    for i in range(N):
        for j in range(N):
            if lst[i][j]:
                home.append([i, j])

    # 최대 집 개수
    max_cnt = 0
    # 좌표 하나씩 돌려
    for i in range(N):
        for j in range(N):
            # 거리에 따른 집 개수 담아(마름모)
            dist = [0] * (2 * N)
            for a, b in home:
                # 마름모는 각 열과 각 행의 차이를 합친 값이 같으면
                # 같은 마름모에 존재
                dist[abs(i - a) + abs(j - b)] += 1

            # 카운팅정렬처럼 더해줌 1은 2마름모크기안에 존재
            for k in range(1, 2 * N):
                dist[k] += dist[k - 1]

            # 떨어진 거리 = k
            # f(k+1)의 k+1인 이유는 0부터 계산하기 때문
            for k in range(0, 2 * N):
                if dist[k] * M - f(k + 1) >= 0:
                    max_cnt = max(max_cnt, dist[k])

    print(f'#{tc} {max_cnt}')