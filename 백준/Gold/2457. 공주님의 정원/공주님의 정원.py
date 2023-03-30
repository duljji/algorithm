import sys
input = sys.stdin.readline
# T= int(input())
# for t in range(1, T+1):
N = int(input())
flst = []
for _ in range(N):
    a, b, c, d = map(int, input().split())
    flst.append((a, b, c, d))
flst.sort(key = lambda x : (x[0], x[1]))
thirty = [4, 6, 9, 11]
thirty_one = [1, 3, 5, 7, 8, 10, 12]
ms = [3, 1] #1월1일 시작하는 것 부터 선택 가능 3월 2일부터는 선택 불가능
me = [3, 1] #최소 3월1일 포함 이후에 종료하는 걸 골라야함
# 꽃을 심을 수 있는 날은 min_month보다 작거나, 같다면 min_day 보다 작아야함
ni = 0
ans = 0
flag = True
while True :
    flag = False
    for i in range(ni, N):
        # 해당 기간에 심을 수 있는지 체크
        sm, sd, em, ed = flst[i]
        if sm < ms[0] or ( sm == ms[0] and sd <= ms[1]) :
            #심을 수 있는 꽃인 경우 em, ed가 더 높은걸 선택
            if em > me[0] or (em == me[0] and ed > me[1] ) : # 현재 고른 꽃보다 더 늦게 종료한다면
                me[0] = em
                me[1] = ed
                ni = i + 1
                flag = True
        else : # 이 이후 나오는 꽃들은 이전 아직 고를 수 없으므로 패스
            #다음번에 돌 때 이번 꽃부터 체크해야하므로 인덱스 저장해둠

            ni = i
            if flag :
                flag = False
                ans += 1
            else :
                flag = True
                ans = 0
            break
    else :
        if not flag :
            break

    if me[0] > 11:
        if flag :
            ans += 1
        break
    if flag : # 만약 11월30일 이상을 가지 못했는데 뽑을 꽃이 없다면 ans = 0 이후 종료
        ans = 0
        break
    #
    # if me[0] in thirty and me[1] == 30 :
    #     ms[0] = me[0] + 1
    #     ms[1] = 1
    # elif me[0] in thirty_one and me[1] == 31 :
    #     ms[0] = me[0] + 1
    #     ms[1] = 1
    # else :
    ms[0] = me[0]
    ms[1] = me[1]
print(ans)




