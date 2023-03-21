import sys
input = sys.stdin.readline
M = int(input())
S = 0
for _ in range(M):
    lst = input().split()
    op = lst[0]
    num = 0
    if len(lst) > 1:
        num = int(lst[1])
    if op == "add":
        S |= (1 << (num - 1))
    if op == "remove":
        S &= ~(1 << (num - 1))
    if op == "check":
        print(1) if S & 1 <<(num-1) else print(0)
    if op == "toggle":
        S ^= (1 << (num - 1))

    if op == "all":
        S = (1 << 20) - 1

    if op == "empty":
        S = 0
