class Solution {
    public int[] solution(int[] num_lst, int n) {
        int[] answer = new int[num_lst.length - n + 1];
        for (int i=0; i<answer.length; i++){
            answer[i] = num_lst[n-1+i];
        }
        return answer;
    }
}