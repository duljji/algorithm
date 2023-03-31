import sys
input = sys.stdin.readline
G = int(input())
P = int(input())
lst = [0] * G
check = True
ans = 0
airs = {i+1 : i+1 for i in range(P+1)}
for _ in range(P):
    air = int(input())
    if check :
        for i in range(airs[air], 0, -1):
            if lst[i-1] == 0 :
                airs[air] = i
                lst[i-1] = 1
                ans += 1
                break
        else :
            check = False
            break
print(ans)





