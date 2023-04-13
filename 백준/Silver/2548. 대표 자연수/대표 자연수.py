N = int(input())

lst = list(map(int, input().split()))
tmp = 10**9
ans = 0
lst.sort()
for i in lst :
    res = 0
    for j in lst:
        res += abs(i-j)
    if tmp > res :
       tmp = res
       ans = i
    
print(ans)

