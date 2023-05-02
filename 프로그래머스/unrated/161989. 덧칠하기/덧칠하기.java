class Solution {
    public int solution(int n, int m, int[] section) {
        int answer = 0;
        int end_num = -1;
        for(int i : section){
            if (i > end_num){
                answer++;
                end_num = i + m -1;
            }
        }
        return answer;
    }
}