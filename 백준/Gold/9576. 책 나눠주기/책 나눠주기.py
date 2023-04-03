T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    lst = []
    v = [0] * (N+1)
    for _ in range(M):
        a, b = map(int, input().split())
        lst.append((a, b))
    lst.sort(key = lambda x : x[1])
    ans = 0
    for i in range(M):
        for j in range(lst[i][0], lst[i][1]+1) :
            if not v[j] :
                v[j] = 1
                ans += 1
                break
    print(ans)

