# 1. 문자열 받아서 앞에서 4개 뒤에서 4개 제거
# 2. 해당 문자열 체크해야 할 알파벳에 추가하기
# 3. 알파벳이 중복될 필요가 없으므로 set으로 중복 제거해주기
# 4. a,n,t,i,c 은 볼 필요가 없으므로 set에서 빼주기
# 5. 만들어진 set 리스트로 바꿔서 하나씩 추가해주면서 K - 5 개를 선택했으면 그 때 해당되는 문자열이 몇개인지 체크하기
# 6.
def dfs(n, lst, cnt):
    global max_ans
    if n == len(c_lst):
        if cnt == K-5 :
            ans = 0
            for S in s_lst :
                for s in S :
                    if s not in lst :
                        break
                else :
                    ans += 1
            max_ans = max(ans, max_ans)

            return
    else :
        dfs(n+1, lst + [c_lst[n]], cnt + 1)
        dfs(n+1, lst, cnt)


N, K = map(int, input().split())
max_ans = 0
base = 0
if K-5 < 0 :
    print(0)
else :
    c_set = set()
    s_lst = []
    for _ in range(N):
        s = input()[4:-4]
        s_set = set(s) - {'a', 'n', 't', 'i', 'c'}
        if len(s_set) == 0 :
            base += 1
        else :
            s_lst.append(list(s_set))

        c_set = c_set.union(s_set)
    c_set -= {'a', 'n', 't', 'i', 'c'}
    if len(c_set) <= K - 5 :
        print(N)
    else :
        c_lst = list(c_set)
        dfs(0, [], 0)
        print(max_ans + base)

