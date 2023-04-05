N = int(input())
lst = []
left = []
right = []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    lst.append([a, b, c, d])
for i in range(N):
    for j in range(N):
        left.append(lst[i][0] + lst[j][1])
        right.append(lst[i][2] + lst[j][3])

left.sort()
right.sort()
rl = len(right) # rl - right의 length
# print(left, right)
ans = 0
for num in left :
    start = 0
    end = rl - 1 # right 안에서 같은 값 찾기
    while start <= end :
        mid = (start + end ) // 2

        if right[mid] + num > 0:
            end = mid - 1
        else :
            start = mid + 1
    upperbound = end
    if upperbound == -1 :
        upperbound = 0




    start = 0
    end = rl - 1
    while start <= end :
        mid = (start + end ) // 2
        if right[mid] + num < 0 :
            start = mid + 1
        else :
            end = mid - 1
    lowerbound = start
    if lowerbound == rl :
        lowerbound = rl -1
    if right[upperbound] + num == 0 or right[lowerbound] +num == 0 :
        ans += 1
        if right[upperbound] + num == 0 and right[lowerbound] + num == 0 :
            ans += upperbound - lowerbound
print(ans)
