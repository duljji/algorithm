N = int(input())

def dfs(k, s_lst, l_lst):
    global min_ans
    if k == N :
        if m == len(s_lst) :
            s_ans = l_ans = 0
            for i in range(N//2):
                for j in range(i+1, N//2):
                    s_ans += board[s_lst[i]][s_lst[j]] + board[s_lst[j]][s_lst[i]]
                    l_ans += board[l_lst[i]][l_lst[j]] + board[l_lst[j]][l_lst[i]]
            min_ans = min(abs(s_ans - l_ans), min_ans)
    else :
        dfs(k+1, s_lst + [k], l_lst)
        dfs(k+1, s_lst, l_lst + [k])
board = [list(map(int, input().split())) for _ in range(N)]

m = N//2
s_lst = []
l_lst = []
min_ans = 100 * 10 * 10
dfs(0, s_lst, l_lst)

print(min_ans)