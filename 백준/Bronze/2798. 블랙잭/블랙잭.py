import sys
input = sys.stdin.readline

N, M = map(int, input().split())

num_list = list(map(int, input().split()))
min_result = M
card_result = 0
for i in range(N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            result = M - (num_list[i] + num_list[j] + num_list[k])
            if min_result > result and result >= 0: 
                min_result = result
             
                card_result = num_list[i] + num_list[j] + num_list[k]

print(card_result)