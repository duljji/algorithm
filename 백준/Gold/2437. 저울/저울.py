N = int(input())
lst = list(map(int, input().split()))

lst.sort()
if lst[0] != 1 :
    print(1)
else :
    ans = 1 # ans의 최솟값은 1
    min_v = 1
    max_v = 1
    for i in range(1, N):
        if min_v + lst[i] > max_v + 1 and lst[i] != max_v+1 :
            break
        else :
            max_v = max_v + lst[i]
    print(max_v + 1)
    
