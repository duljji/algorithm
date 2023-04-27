class Solution {
    public int solution(int slice, int n) {
        int answer = 1;
        int total = slice;
        while (total < n){
            answer += 1;
            total += slice;
        }
        return answer;
    }
}