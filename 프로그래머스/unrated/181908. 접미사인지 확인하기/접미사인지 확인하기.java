class Solution {
    public int solution(String my_string, String is_suffix) {
        int answer = 0;
        int ml = my_string.length();
        int tl = is_suffix.length();
        if (ml < tl){
return 0;}
        answer = 1;
        for (int i=ml-tl; i<my_string.length(); i++){
            if (my_string.charAt(i) != is_suffix.charAt(i-(ml-tl))){
                answer = 0;
                break;
            }
        }
        return answer;
    }
}