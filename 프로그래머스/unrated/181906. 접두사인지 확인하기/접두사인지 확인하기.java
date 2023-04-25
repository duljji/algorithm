class Solution {
    public int solution(String my_string, String is_prefix) {
        int answer = 0;
        if (my_string.indexOf(is_prefix) == 0){
            answer =1;
        }
        return answer;
    }
}