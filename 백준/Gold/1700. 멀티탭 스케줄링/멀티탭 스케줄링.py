N, K = map(int, input().split())

lst = list(map(int, input().split()))

v = [0] * N
ans = 0
start = 0
for i in range(K):
    if 0 in v:
        if lst[i] in v :
            continue
        v[v.index(0)] = lst[i]
        start = i + 1
    else :
        start = i
        break
for i in range(start, K):
    tmp = set() #임시 리스트 만들기
    if lst[i] not in v : #꽂을 수 있는 콘센트가 없다면
        ans += 1
        for j in range(i+1, K): #앞으로 나올 콘센트 넣기
            if lst[j] in v :
                tmp.add(lst[j])
                if len(tmp) == N : #현재 꽂혀져있는 콘센트 중 가장 나중에 나오는 코드 뽑기
                    v[v.index(lst[j])] = lst[i]
                    break
        else :
            for j in range(len(v)):
                if v[j] not in tmp :
                    v[j] = lst[i]
                    break

print(ans)






