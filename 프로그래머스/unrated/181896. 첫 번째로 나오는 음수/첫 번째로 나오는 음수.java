class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        boolean check = true;
        for (int i=0; i<num_list.length; i++){
            if (num_list[i] < 0){
                check = false;
                answer = i;
                break;
            } 
        }
        if (check) {
            answer = -1;
        }
        
        return answer;
    }
}