a, b = map(int, input().split())
lst = [True] * (b-a+1)

for i in range(2, int(b**0.5)+1):
    tmp = i * i

    #a 에서 해당 제곱수로 나누어떨어지는 가장 가까운 수 찾기
    mod = a % tmp
    target = a
    if mod != 0 :
        target = target - mod + tmp

    #target을 찾았으면 그 값부터 b까지 tmp를 증가시키면서 False 처리
    for j in range(target, b+1, tmp):
        lst[j-a] = False

print(sum(lst))