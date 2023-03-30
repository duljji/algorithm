import heapq
import sys

input = sys.stdin.readline
N = int(input())
num_heap = []
for n in range(N):
    heapq.heappush(num_heap, int(input()))
result = 0
while num_heap :
    if len(num_heap) == 1 :
        break
    else :
        n = heapq.heappop(num_heap) + heapq.heappop(num_heap)
        result += n
        heapq.heappush(num_heap, n)
print(result)