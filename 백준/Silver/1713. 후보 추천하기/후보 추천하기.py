N = int(input())
M = int(input())
plst = []
slst = list(map(int, input().split()))
v = [0] * 101
for i in slst :
    if len(plst) < N :
        if i not in plst :
            plst.append(i)
        v[i] += 1
    else :
        if i in plst :
            v[i] += 1
        else :
            min_v = 10000
            idx = 0
            for j in plst:
                if min_v > v[j] :
                    min_v = v[j]
                    idx = j
            plst.remove(idx)
            v[idx] = 0
            plst.append(i)
            v[i] += 1

print(*sorted(plst))