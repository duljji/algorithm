import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    c_lst = list(map(int, input().split()))
    c_lst.sort(reverse=True)

    #M초마다 K개의 붕어빵을 만든다.
    time = 0
    bread = 0
    check = True
    if c_lst[-1] == 0 :
        check = False
    while check :
        time += 1 #1초가 흐르고
        if time % M == 0 : #M초가 흘렀으면 K개의 붕어빵 생성
            bread += K
        if c_lst :
            while c_lst and c_lst[-1] == time : # 현재 시간에 도착한 손님이 존재하면 붕어빵을 줄 수 있는지 판단
                if bread : #붕어빵이 남아있으면
                    c_lst.pop()
                    bread -= 1
                else : #붕어빵이 없으면
                    check = False
                    break

        else : # 기다리는 손님이 없으면
            break

    if check :
        print(f"#{tc}", "Possible")
    else :
        print(f"#{tc}", "Impossible")