def solution(weights):
    answer = 0
    dp1 = [0] * 1001
    dp2 = [0] * 4001
    
    for i in range(0, len(weights)) :
        dp1[weights[i]] += 1
    
    for i in range(0, len(dp1)):
        if dp1[i] != 0 :
            for j in range(0, dp1[i]):
                answer += j
    
    for i in range(0, len(dp1)) :
        if dp1[i] != 0 :
            answer += dp2[i*2] * dp1[i]
            answer += dp2[i*3] * dp1[i]
            answer += dp2[i*4] * dp1[i]
            dp2[i*2] += dp1[i]
            dp2[i*3] += dp1[i]
            dp2[i*4] += dp1[i]
    
        
                
    return answer
        