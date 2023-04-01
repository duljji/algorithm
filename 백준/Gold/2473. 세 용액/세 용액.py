'''
5
999999999 1000000000 1000000000 1000000000 1000000000

'''
N = int(input())

lst = sorted(list(map(int, input().split())))
ans = 3000000001
cv = 0
ans_A, ans_B, ans_C = 0,0, 0
A = 0
B =  A+1
C = N - 1
while A < N-2 :
    B = A + 1
    C = N - 1
    while B != C :
        tmp = lst[A] + lst[B] + lst[C]
        if abs(tmp) < abs(ans) :
            ans = tmp
            ans_A, ans_B, ans_C = A, B, C
        if tmp > 0 :
            C -= 1
        elif tmp < 0 :
            B += 1
        else :
            break
    if ans == 0 :
        break
    A += 1
print(lst[ans_A], lst[ans_B], lst[ans_C])



