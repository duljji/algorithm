N = int(input())
lst = []
for _ in range(N):
    lst.append(int(input()))
lst.sort()
left = []
right = []
for i in range(N):
    for j in range(i, N):
        left.append(lst[i]+lst[j])

for i in range(N-1, -1, -1):
    for j in range(i+1):
        right.append([lst[i]-lst[j], i])
m = len(left)
left.sort()
right.sort(reverse=True)
ans = 0
for res, i in right:
    s = 0
    e = m -1
    flag = False
    while s <= e :
        mid = (s + e)//2
        if left[mid] == res :
            ans = max(ans, lst[i])
            break
        elif left[mid] > res :
            e = mid - 1
        else :
            s = mid + 1
print(ans)