N, M = map(int, input().split())

lst = [99999] * 100002
lst[N] = 0
for i in range(N - 1, -1, -1):  # 현재 위치에서 아래로 내려가는 경우는 순간이동을 할 수 없으므로 현재 시간에서 +1을 해주면 된다
    lst[i] = lst[i + 1] + 1
for i in range(100001):
    j = i
    while j < 100001:
        if j != 0 and  lst[j - 1] > lst[j] + 1:
            lst[j - 1] = lst[j] + 1
        if  lst[j + 1] > lst[j] + 1:
            lst[j + 1] = lst[j]+ 1
        if j * 2 < 100001 and lst[j * 2] > lst[j] + 1:
            lst[j * 2] = lst[j] + 1
        j *= 2
        if j == 0 :
            break
i = M
ans = [M]
while lst[i] != 0:
    if i == 0 :
        i = 1
        ans.append(i)

        continue
    if lst[i + 1] > lst[i - 1]:
        next_i = i - 1
    else :
        next_i = i + 1

    if i % 2 == 0 and lst[next_i] > lst[i // 2]:
        next_i = i // 2

    ans.append(next_i)
    i = next_i


print(len(ans) - 1)
for i in range(len(ans) - 1, -1, -1):
    print(ans[i], end=' ')
