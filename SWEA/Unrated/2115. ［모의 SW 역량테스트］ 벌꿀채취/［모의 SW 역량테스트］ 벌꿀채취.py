def combinations(k, lst, n_lst):
    global max_v
    if k == M :
        if sum(n_lst) <= C :
            ans = 0
            for i in range(len(n_lst)):
                ans += n_lst[i] ** 2
            max_v = max(ans, max_v)
        return
    else :
        combinations(k+1, lst, n_lst + [lst[k]])
        combinations(k+1, lst, n_lst)


T = int(input())

for tc in range(1, T+1):
    N, M, C = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]
    alst = []
    blst = []
    max_ans = 0
    for i in range(N):
        for j in range(N-M+1):
            alst = board[i][j:j+M]
            for _ in range(M):
                visited[i][j+_] = True
            # A일꾼이 채집할 벌꿀 선택 완료했으면 B일꾼 선택
            for r in range(N):
                for c in range(N-M+1):
                    for _ in range(M):
                        if visited[r][c+_] == True :
                            break
                    else :
                        blst = board[r][c:c+M]
                        #alst와 blst중 합이 C 이하가 되는경우를 Combination 돌리기
                        max_v = 0
                        combinations(0, alst, [])
                        max_a = max_v
                        max_v = 0
                        combinations(0, blst, [])
                        max_b = max_v
                        max_ans = max(max_ans, max_a + max_b)
            for _ in range(M):
                visited[i][j+_] = False
    print(f"#{tc}", max_ans)
