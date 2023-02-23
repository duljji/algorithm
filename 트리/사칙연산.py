import sys

sys.stdin = open('input.txt')

T = 10

for tc in range(1, T + 1):
    N = int(input())
    Tree = [0] * (N + 1)
    c1 = [0] * (N + 1)
    c2 = [0] * (N + 1)
    for _ in range(N):
        node, value, *child = input().split()
        node = int(node)

        if len(child) > 1 :
            c1[node] = int(child[0])
            c2[node] = int(child[1])
        elif child :
            c1[node] = int(child[0])

        Tree[node] = value
    def inorder(t):
        if t :
            left = inorder(c1[t])
            right = inorder(c2[t])
        if Tree[t] == "+" :
            Tree[t] = int(left) + int(right)
        elif Tree[t] == "-":
            Tree[t] = int(left) - int(right)
        elif Tree[t] == "*" :
            Tree[t] = int(left) * int(right)
        elif Tree[t] == "/" :
            Tree[t] = int(left) / int(right)
        else :
            return Tree[t]
        return Tree[t]
    print(f"#{tc}", int(inorder(1)))

