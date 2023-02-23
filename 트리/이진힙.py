import sys
sys.stdin= open("input.txt")

def enq(item):
    global last
    last += 1
    heap[last] = item
    c = last
    p = c // 2
    while p and heap[p] > heap[c] :
        heap[p], heap[c] = heap[c], heap[p]
        c = p
        p = c // 2
    return


T = int(input())
for tc in range(1, T+1):
    N = int(input()) #힙의 사이즈
    last = 0
    heap = [0] * (N+1) # 1번 노드부터
    n_lst = list(map(int, input().split()))
    for i in range(len(n_lst)) :
        enq(n_lst[i])

    last = N//2
    ans = 0
    while last != 0 :
        ans += heap[last]
        last //= 2
    print(f"#{tc}", ans)

