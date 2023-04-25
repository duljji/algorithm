class Solution {
    public int solution(String my_string, String target) {
        int answer = 0;
        boolean check = true;
        if (target.length() > my_string.length()){
            answer = 0;
        } else {
            for (int i=0; i<= my_string.length() - target.length(); i++){
                check = true;
                for (int j=0; j<target.length(); j++){
                    if (my_string.charAt(i+j) != target.charAt(j)){
                        check = false;
                        break;
                    }
                }
                if (check) {
                    answer = 1;
                    break;
                }
            }
            
        }
        return answer;
    }
}