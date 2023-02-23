import sys
sys.setrecursionlimit(10001)
n_lst = []
while True :
    try :
        n = int(input())
    except :
        break
    if n == "" :
        break
    n_lst.append(n)
Tree = [0] * (len(n_lst) + 1)
c1 = [-1] * (len(n_lst) + 1)
c2 = [-1] * (len(n_lst) + 1)
stack = [0] #스택에는 루트노드의 인덱스가 들어있음
idx = 0
for i in range(1, len(n_lst)): #이전에 들어온 값보다 작으면 왼쪽 child인 것

    if n_lst[stack[-1]] > n_lst[i] :
        c1[stack[-1]] = i
        stack.append(i)
    else : # 이전에 들어온 값보다 크면 오른쪽 노드!
        #나보다 작은 값 중 가장 큰 값의 오른쪽으로 들어가야함
        while stack and n_lst[stack[-1]] < n_lst[i] :
            idx = stack.pop() #나보다는 작으면서 가장 큰 값의 오른쪽 노드
        c2[idx] = i
        stack.append(i)

def postorder(t):
    if t >= 0 :
        postorder(c1[t])
        postorder(c2[t])
        print(n_lst[t])

postorder(0)