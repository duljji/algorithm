N, M = map(int, input().split())

num_list = list(map(int, input().split()))
num_list.sort()
#중복 가능하면서 순서 상관 없고, 
stack = []
def dfs(start):

    if M == len(stack):
        print(*stack)
        return
    else:
        check_num = 0
        for i in range(len(num_list)):
            if check_num == num_list[i] or start > num_list[i] :
                continue
            stack.append(num_list[i])
            dfs(num_list[i])
            stack.pop()
            check_num = num_list[i]
dfs(0)