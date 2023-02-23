import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    V, M, L = map(int, input().split()) #노드의 개수, 리프노드의개수, 출력할 노드
    Tree = [0] * (V+1)
    c1 = [0] * (V+1)
    c2 = [0] * (V+1)

    for i in range(1, (V)//2+1):
        p = i
        print(p)
        c1[p] = p*2
        if p*2 + 1 <= V:
            c2[p] = p*2+1
    for _ in range(M):
        node, val = map(int, input().split())
        Tree[node] = val
    def postorder(t):
        if t :
            left = postorder(c1[t])
            right = postorder(c2[t])
            if t == 5 :
                print(left, c1[t], right, c2[t])
            Tree[t] = Tree[t] + left + right

            return Tree[t]
        else :
            return 0
    postorder(1)
    print(Tree[L])