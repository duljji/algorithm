class Solution {
    public int[] solution(long n) {
        String N = String.valueOf(n);
        int[] answer = new int[N.length()];
        int idx = 0;
        while (n!=0){
            answer[idx] = (int) (n%10);
            n /= 10;
            idx +=1;
        }
        
        return answer;
    }
}