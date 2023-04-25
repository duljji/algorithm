class Solution {
    public int solution(int[] num_list) {
        int answer = 0;
        int hab = 0;
        int gob = 1;
        for (int i=0; i<num_list.length; i++){
            hab += num_list[i];
            gob *= num_list[i];
            
        }
        if (hab*hab > gob){
            answer =1;
        } 
        return answer;
    }
}