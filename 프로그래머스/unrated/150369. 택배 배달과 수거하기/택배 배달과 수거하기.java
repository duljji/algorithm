class Solution {
    public long solution(int cap, int n, int[] deliveries, int[] pickups) {
        long answer = 0;
        int d_cap = cap;
        int p_cap = cap;
        int d_cnt = 0;
        int p_cnt = 0;
        boolean p_check = false;
        boolean d_check = false;
        for(int i=n-1 ; i>=0; i--){
            if(p_cap == cap && pickups[i]!=0){
                p_cnt++;
                if(p_cnt > d_cnt){
                    answer += (i+1)*2;
                }
            }
            if(d_cap == cap && deliveries[i] != 0){
                d_cnt++;
                if(d_cnt > p_cnt){
                    answer += (i+1)*2;
                }
            }
            if(d_cap >= deliveries[i]){
                d_cap -= deliveries[i];
                deliveries[i] = 0;
            }else {
                deliveries[i] -= d_cap;
                d_cap = cap;
                d_check = true;
                
            }
            if(p_cap >= pickups[i]){
                p_cap -= pickups[i];
                pickups[i] = 0;
            } else {
                pickups[i] -= p_cap;
                p_cap = cap;
                p_check = true;
            }
         
            if(d_check || p_check){
                i++;
                d_check = false;
                p_check = false;
            }
            
        }
        return answer;
    }
}