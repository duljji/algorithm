
N, M = map(int, input().split())

lst = [0] * 100002
lst[N] = 1
for i in range(N-1, -1, -1): #현재 위치에서 아래로 내려가는 경우는 순간이동을 할 수 없으므로 현재 시간에서 +1을 해주면 된다
    lst[i] = lst[i+1] + 1

for i in range(100001): # 이제 만들어둔 시간 셋팅으로 2배수의 값들을 모두 최솟값으로 설정해준다
    if lst[i] != 0 : #이미 만들어둔 셋팅이 있는 경우 최솟값 셋팅해주기
        # 해당 위치에서 1초 걸려 걸어갈 수 있는 경우 2가지
        j = i
        while j < 100001 :
            #해당 위치에서 0초만에 갈 수 있는 경우
            if lst[j] == 0 or lst[j] > lst[i] : #다른 칸에서 이동하지 않았거나 다른 칸에서 이동하는 것보다 빠르게 이동할 수 있는 경우
                lst[j] = lst[i]
            if lst[j + 1] == 0 or lst[j + 1] > lst[j] + 1:
                lst[j + 1] = lst[i] + 1
            if j == 0 :
                break
            if lst[j - 1] == 0 or lst[j - 1] > lst[j] + 1:
                lst[j - 1] = lst[j] + 1
            j *= 2

print(lst[M]-1)

