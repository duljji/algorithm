import sys

input = sys.stdin.readline

total_price = int(input())

#일단 5원으로 최대한 거슬러주기

five_cnt = total_price // 5 #5원으로 최대한 거슬러 준 개수
two_cnt = (total_price % 5) // 2 # 2원으로 최소한 거슬러 준 개수
remaining_price = (total_price % 5) % 2
while True :
    #만약 남아있는 돈이 없으면 동전 개수 출력하고 break
    if remaining_price == 0 :
        print(five_cnt + two_cnt)
        break
    else : #이렇게 했는데 나머지가 있으면 five_cnt 하나씩 줄여보기
     five_cnt -= 1
     two_cnt = (total_price - 5 * five_cnt) // 2
     remaining_price = (total_price - 5 * five_cnt) % 2
    #five_cnt가 -1개가 되면 모든 경우의 수로도 나눌 수 없다는 뜻이므로 -1 출력
    if five_cnt <= -1 :
        print(-1)
        break

