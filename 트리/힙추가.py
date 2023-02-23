def enq(n):
    global last
    last += 1
    heap[last] = n
    c = last
    p = c//2
    while p > 0 and heap[p] < heap[c] :
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2

def deq():
    global last
    tmp = heap[1] #루트 임시저장
    heap[1] = heap[last] # 마지막 정점의 값을 루트로 이동
    last -= 1
    p = 1
    c = p * 2
    while p <= last
        if c + 1 <= last and heap[c]  <  heap[c+1] :
            c = c + 1

        if heap[p] heap[c]




heap = [0] * 101
last = 0
enq(5)
print(heap)
enq(15)
print(heap)
enq(8)
print(heap)
enq(20)
print(heap)
