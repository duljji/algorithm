N = int(input())
# 1. 메모이제이션을 해야하는데 그 전 수도 기록을 해주어야함
memo = [[99999, 0] for _ in range(N+1)]
memo[1] = [0, 0]

for i in range(1, N):
    # 해당 값에서 1을 더해서 1로 올수 있는지 확인
    if memo[i + 1][0] > memo[i][0] + 1:
        memo[i + 1] = [memo[i][0] + 1, 1]
    if i*3 <= N and memo[i * 3][0] > memo[i][0] + 1 :
        memo[i*3] = [memo[i][0] + 1, 3]
    if i*2 <= N and memo[i*2][0] > memo[i][0] + 1 :
        memo[i*2] = [memo[i][0] + 1, 2]

print(memo[N][0])
i = N
while True:
    print(i, end=' ')
    if memo[i][1] == 3 :
        i //=3
    elif memo[i][1] == 2 :
        i //=2
    elif memo[i][1] == 1 :
        i -= 1
    else :
        break
