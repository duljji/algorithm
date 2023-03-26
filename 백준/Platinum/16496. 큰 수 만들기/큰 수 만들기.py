N = int(input())

num = input().split()

for i in range(len(num)-1, -1, -1):
    for j in range(i):
        if int(num[j] + num[j+1]) < int(num[j+1] + num[j]) :
            num[j], num[j+1] = num[j+1], num[j]
print(int(''.join(num)))
