N, M = map(int, input().split())
road_list = []
for _ in range(N):
    road = list(map(int, input().split()))
    road_list.append(road)
chicken_house = []
house = []
for i in range(N):
    for j in range(N):
        if road_list[i][j] == 2 :
            chicken_house.append([i, j])

        if road_list[i][j] == 1:
            house.append([i, j])
#house 전체를 돌면서 chicken_house와의 거리를 구하면 됨
#chicken_house는 총 M개만 선택할 수 있음
stack = []
visited = [False] * len(chicken_house)
city_chicken_distance = 1e9
def dfs(start):
    global city_chicken_distance
    if len(stack) == M:
        result = 0
        for x, y in house:
            min_chicken_house = 1e9
            for cx, cy in stack:
                chicken_distance = abs(cx-x) + abs(cy-y)
                min_chicken_house = min(min_chicken_house, chicken_distance)
            result += min_chicken_house
        city_chicken_distance = min(result, city_chicken_distance) 
        return
    else:
        for i in range(len(chicken_house)): #chicken_house 조합
            if not visited[i] and start <= i :
                visited[i] = True
                stack.append(chicken_house[i])
                dfs(i+1)
                visited[i] = False
                stack.pop()
dfs(0)
print(city_chicken_distance)