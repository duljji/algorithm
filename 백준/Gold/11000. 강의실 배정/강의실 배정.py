# 강의실 수업의 시작시간과 종료시간이 주어진다
# 종료시간이 가장 짧은 강의실(최소힙으로 꺼내기)의 종료시간보다
# 작은 값이 시작시간으로 들어오면 ? 강의실을 하나 추가로 쓰고 최소힙에 그 강의실도 넣는다
import heapq
import sys
input = sys.stdin.readline
N = int(input()) #강의 개수 받기
room_list = []
time_list = []
max_room = 0
need_pop = True
for n in range(N):
    heapq.heappush(time_list, list(map(int, input().split()))) #강의 시작시간 기준의 최소힙
 #강의실 배정
min_end = heapq.heappop(time_list)[1]
heapq.heappush(room_list, min_end) # 강의실 배정

need_pop = False
cnt = 1
while time_list : 
    min_end = heapq.heappop(room_list) #현재 강의실들 중 가장 빨리 끝나는 시간 체크

    start_time, end_time = heapq.heappop(time_list) #가장 빨리 시작하는 과목과 시간 비교

    if min_end <= start_time: #강의실이 비어있으면
        heapq.heappush(room_list, end_time) #강의실 종료 시간 업데이트
    else : #강의실이 비어있지 않으면
        heapq.heappush(room_list, end_time) #방 추가
        cnt += 1 #방 개수 1 증가
        heapq.heappush(room_list, min_end) #기존 강의실도 다시 넣어주기 (추가 된 강의실이 먼저 끝날 수 있으므로 다시 뽑아줘야함)
print(cnt)

