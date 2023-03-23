
N = int(input())
Map = []
for n in range(N):
    Map.append(list(map(int, input().split())))
visited = [False] * N
min_score = 1e9
stack = []


def dfs(result):
    global min_score
    if len(stack) == N:

        if Map[stack[-1]][stack[0]] == 0 :
            result += 1e9
        else :
            result += Map[stack[-1]][stack[0]]
        min_score = min(min_score, result)

        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = True
                stack.append(i)
                if len(stack) < 2:
                    tmp_result = result
                    dfs(tmp_result)
                elif Map[stack[-2]][stack[-1]] != 0:
                    tmp_result = result + Map[stack[-2]][stack[-1]]
                    dfs(tmp_result)

                visited[i] = False
                stack.pop()


dfs(0)
print(min_score)
