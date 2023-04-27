import java.util.*;
class Solution {
    public String solution(String my_string) {
        String answer = "";
        StringBuilder sb = new StringBuilder();
        sb.append(my_string);
        answer = sb.reverse().toString();

        return answer;
    }
}