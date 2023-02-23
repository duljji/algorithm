N = int(input())

a_to_num = {chr(i) : i - ord("A") + 1 for i in range(ord("A"), ord("Z") + 1)}
c1 = [0] * (N+1)
c2 = [0] * (N+1)
for _ in range(1, N+1):
    parent, *child = input().split()
    parent = a_to_num[parent]
    if child[0] != "." :
        c1[parent] = a_to_num[child[0]]
    if child[1] != "." :
        c2[parent] = a_to_num[child[1]]

def preorder(t):
    if t :
        print(chr(ord("A") + t - 1), end="")
        preorder(c1[t])
        preorder(c2[t])
def inorder(t):
    if t :
        inorder(c1[t])
        print(chr(ord("A") + t - 1), end="")
        inorder(c2[t])
def postorder(t):
    if t :
        postorder(c1[t])
        postorder(c2[t])
        print(chr(ord("A") + t - 1), end="")

preorder(1)
print()
inorder(1)
print()
postorder(1)

