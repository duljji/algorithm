import sys
input = sys.stdin.readline

N = int(input())
num_list = []
for n in range(N):
    A, B = list(map(int, input().split()))
    num_list.append([A,B])
num_list.sort(key = lambda x : (x[1], x[0]))
cnt = 0
select_num = 0
for i in range(N):
    if num_list[i][0] >= select_num :
        cnt += 1

        select_num = num_list[i][1]

print(cnt)