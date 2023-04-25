class Solution {
    public int solution(String myString, String pat) {
        int answer = 0;
        boolean check = true;
        myString = myString.toLowerCase();
        pat = pat.toLowerCase();
        if (myString.length() < pat.length()){
            check = false;
        }
        for (int i=0; i<=(myString.length()-pat.length()); i++){
            check = true;
            for (int j =0; j<pat.length(); j++){
                if (myString.charAt(i+j) != pat.charAt(j)){
                    check = false;
                }
            }
            if (check) break;
        }
        if (check){
            answer = 1;
        }
        return answer;
    }
}