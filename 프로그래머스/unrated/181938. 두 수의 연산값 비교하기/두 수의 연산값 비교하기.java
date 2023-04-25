class Solution {
    public int solution(int a, int b) {
        int answer = 0;
        String tmp = "";
        tmp = Integer.toString(a) + Integer.toString(b);
        answer = Integer.valueOf(tmp);
        answer = answer > 2*a*b ? answer : 2*a*b;
        return answer;
    }
}