class Solution {
    boolean solution(String s) {
        boolean answer = true;

        // [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
        if(s.replaceAll("p|P", "").length() == s.replaceAll("y|Y", "").length()){
            answer = true;
        } else {
            answer= false;
        }

        return answer;
    }
}