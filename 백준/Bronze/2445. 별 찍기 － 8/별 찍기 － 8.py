N = int(input())

for i in range(N-1, -1, -1):
    print('*'*(N-i), end="")
    print(' '*i*2, end = "")
    print('*'*(N-i))
for i in range(1, N):
    print("*" * (N-i), end = "")
    print(" "* i * 2, end = "")
    print("*" * (N-i))

