# 파이썬에서 제공하는 라이브러리는 최소힙이 기본
import heapq
hq = []

# 기본
# 응용
heapq.heappush(hq, (-4, 4))
heapq.heappush(hq, (-3, 3))
heapq.heappush(hq, (-2, 2))
heapq.heappush(hq, (-1, 1))

for i in range(4):
    print(heapq.heappop(hq)[1], end = " ")