import sys
input = sys.stdin.readline
N = int(input())
c_stack = []
q_dict = {i+1 : [] for i in range(N)}

for _ in range(1, N+1):
    op, *num = input().rstrip().split()
    if num :
        num = int(num[0])
    if op == 'a' :
        c_stack.append(num)
    elif op == 's' :
        if c_stack :
            c_stack.pop()
    elif op == 't' :
        c_stack = q_dict.get(num-1, [])[:]


    if c_stack :
        print(c_stack[-1])
        q_dict[_] = c_stack[:]
    else :
        print(-1)