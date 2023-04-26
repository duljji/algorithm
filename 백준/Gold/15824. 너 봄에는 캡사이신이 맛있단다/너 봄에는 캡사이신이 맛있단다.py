N = int(input())

lst = sorted(list(map(int, input().split())))

start = 0
end = N-1
ans = 0
while start != end :
    for i in range(end, start, -1):
        ans += (lst[i] - lst[start]) * 2**(i - start-1)
    start += 1
print(ans%1000000007)

