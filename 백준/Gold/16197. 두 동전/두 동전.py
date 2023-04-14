def is_drop(r, c):
    return not (0 <= r < R and 0 <= c < C)
def dfs(k, ar, ac, br, bc):
    global ans
    if k > ans :
        return
    if k == 10 :
        return
    for d in range(4):
        nar = ar + dr[d]
        nac = ac + dc[d]
        nbr = br + dr[d]
        nbc = bc + dc[d]
        #둘 중 하나가 떨어졌을 경우 더 진행하지 않음
        if is_drop(nar, nac) ^ is_drop(nbr, nbc):
            ans = min(k, ans)
        #둘 다 떨어졌거나 둘 다 안떨어진 경우 두 가지로 나눠서 처리하기
        elif is_drop(nar, nac) and is_drop(nbr, nbc) : # 둘 다 떨어졌다면 해당 경우는 제외해야하므로 dfs 돌리지 않음
            continue
        else : # 둘 다 떨어지지 않았을 경우 다음 버튼 눌러보기
            if arr[nar][nac] == "#" :
                nar = ar
                nac = ac
            if arr[nbr][nbc] == "#" :
                nbr = br
                nbc = bc
            dfs(k+1, nar, nac, nbr, nbc)





R, C = map(int, input().split())
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
arr = [input() for _ in range(R)]
flag = False
for i in range(R):
    for j in range(C):
        if arr[i][j] == 'o' and not flag :
            ar, ac = i, j
            flag = True
        elif arr[i][j] =='o' and flag :
            br, bc = i, j
INF = 11
ans = INF
dfs(0, ar, ac, br, bc)
if ans == INF :
    print(-1)
else :
    print(ans+1)
