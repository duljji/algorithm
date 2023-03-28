N = int(input())

lst = list(map(int, input().split()))
lst = [0] + lst
fv = 0
ans = 1
memo = [0] * (N+1)
for i in range(1, N+1):
    memo_idx = 0
    for j in range(i+1):
        if lst[j] < lst[i] and memo[memo_idx] < memo[j] :
            memo_idx = j

    memo[i] = memo[memo_idx] + 1
print(max(memo))



