import random
import time
heap = [0] * 101
last = 0

def enq(item):
    #삽입을 했다면 마지막 위치를 수정해야함
    global last

    last += 1 # 마지막 위치에 원소 추가
    heap[last] = item

    # 추가를 하고 나서 부모노드 > 자식 노드를 만족하도록 해야한다.
    c = last # 현재 위치를 자식으로 생각
    p = c // 2 # 부모노드의 위치 계산
    # 자식이 부모보다 작을 때까지 위치를 바꿔준다.
    while p and heap[p] < heap[c] : # p가 0이 아니면서 자식이 부모보다 더 큰경우
        heap[p], heap[c] = heap[c], heap[p]
        # 자리를 바꿨으면
        c = p
        p = c // 2

    return
def deq():
    global last
    #루트노드 삭제
    root = heap[1]
    heap[1] = heap[last]
    last -= 1 # 마지막 원소의 위치 하나 줄어들음
    #루트부터 자리 찾기 시작
    p = 1
    c = p * 2
    while c <= last: #자식의 위치가 last 보다 작은 경우 그 중 큰 값보다 큰지 체크
        if heap[c] < heap[c+1] :
            c += 1
        if heap[p] < heap[c] : # 자식이 더 크면 자리 체인지
            heap[p], heap[c] = heap[c], heap[p]
        p = c
        c = p * 2

    return root
for i in range(10):
    enq(random.randrange(1, 101))
print(heap)
start = time.time()
idx = 0
for i in range(1, 11):
    for j in range(i, 11):


start = time.time()
for i in range(10):
    print(deq())
end = time.time()

