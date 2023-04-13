def find_bottom(top_idx):
    bottom_idx = 0
    if top_idx == 0:
        bottom_idx = 5
    elif top_idx == 1:
        bottom_idx = 3
    elif top_idx == 2:
        bottom_idx = 4
    elif top_idx == 3:
        bottom_idx = 1
    elif top_idx == 4:
        bottom_idx = 2
    elif top_idx == 5:
        bottom_idx = 0

    return bottom_idx


N = int(input())

dice = [list(map(int, input().split())) for _ in range(N)]
s_lst = [[1, 2, 3, 4], [2, 0, 4, 5], [1, 5, 3, 0], [5, 4, 0, 2], [0, 3, 5, 1], [4, 3, 2, 1]]
top_idx = -1
max_ans = 0
for i in range(6):  # 주사위 top값이 어디를 바라볼지 설정
    ans = 0
    top_idx = i
    bottom_idx = find_bottom(top_idx)
    top_v = dice[0][top_idx]
    bottom_v = dice[0][bottom_idx]
    lst = s_lst[i]
    max_cnt = 0
    for j in range(4):
        cnt = dice[0][lst[j]]
        max_cnt = max(cnt, max_cnt)
    ans += max_cnt

    for n in range(N - 1):
        top_idx = dice[n + 1].index(bottom_v)
        bottom_idx = find_bottom(top_idx)
        top_v = dice[n+1][top_idx]
        bottom_v = dice[n+1][bottom_idx]
        lst = s_lst[top_idx]
        max_cnt = 0
        for j in range(4):
            cnt = dice[n+1][lst[j]]
            max_cnt = max(cnt, max_cnt)
        ans += max_cnt
    max_ans = max(ans, max_ans)
print(max_ans)

