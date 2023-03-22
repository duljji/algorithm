def f(n):
    if memo[n] != 0:
        return memo[n]
    else :
        memo[n] = f(n-1) + f(n-2) + f(n-3)

        return memo[n]

memo = [0] * 11

memo[0] = 1
memo[1] = 2
memo[2] = 4

N = int(input())

for _ in range(N):
    n = int(input())
    print(f(n-1))