class Solution {
    public int solution(int[] num_list, int n) {
        int answer = 0;
        boolean check = false;
        for(int i=0; i< num_list.length; i++){
            if (num_list[i] == n){
                check = true;
            }
        }
        if (check){
            answer = 1;
        } else {
            answer = 0;
        }
        return answer;
    }
}