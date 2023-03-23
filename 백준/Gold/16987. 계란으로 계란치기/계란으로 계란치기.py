# 1. 가장 왼쪽부터 계란을 하나 든다
# 2. 본인을 제외한 계란 중 칠 수 있는 경우를 모든 경우를 다 한번씩 쳐본다
# 3. 계란을 쳤을 경우 다음 계란을 선택해서 또 자신을 제외한 모든 계란을 한번씩 다 쳐본다
# 4. 계란이 깨졌을 경우 방문처리를 해서 계란을 치지 않도록 한다

def dfs(n, cnt): #n번째 계란을 선택해서 칠 수 있는 계란 모두 쳐보기
    global max_ans
    # 내려칠 계란이 깨져있는 상태면 다음 계란 선택하기
    if cnt + (N-n)*2 < max_ans :
        return
    if n == N :
        max_ans = max(cnt, max_ans)
        return
    # 현재 선택한 계란이 이미 깨져있는 상태라면 다음계란 선택하기
    if e_lst[n][0] <= 0 :
        dfs(n+1, cnt)
    else :
        flag = False
        for i in range(N): #내려칠 계란 탐색하기
            #만약 내려칠 계란이 현재 계란이라면 넘어가기
            if n == i or e_lst[i][0] <= 0 :
                continue
            #해당 계란이 깨져있는 상태라면 또 넘어가기
            flag = True
            # 해당 계란을 내려칠 수 있다면 내려치고 다음 계란 선택하기
            e_lst[n][0] -= e_lst[i][1]
            e_lst[i][0] -= e_lst[n][1]
            dfs(n+1, cnt+int(e_lst[n][0]<=0)+int(e_lst[i][0]<=0))
            # 다음 계란을 내려칠 때 이전에 내려쳤던 값 초기화해주기
            e_lst[n][0] += e_lst[i][1]
            e_lst[i][0] += e_lst[n][1]
        if flag == False :
            dfs(n+1, cnt)


N = int(input())
e_lst = []
for _ in range(N):
    S, W = map(int, input().split())
    e_lst += [[S,W]]
max_ans = 0
dfs(0, 0)
print(max_ans)