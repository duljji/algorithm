import java.util.*;
class Solution {
    public int solution(int[] picks, String[] minerals) {
        int answer = 0;
        int cnt = 0;
        int idx = 0;
        int tmp_value = 0;
        
        int total_mine = 0;
        for(int i=0; i<picks.length; i++){
            total_mine += picks[i];
        }
        int[] values = new int[total_mine];
        for(int i=0; i<total_mine*5; i++){
            cnt++;
            if(minerals[i].equals("diamond")){
                tmp_value += 31;
            }else if (minerals[i].equals("iron")){
                tmp_value += 6;
            }else {
                tmp_value += 1;
            }
            if ( i == minerals.length-1){
                values[idx++] = tmp_value;
                tmp_value = 0;
                cnt = 0;
                break;
            }
            if(cnt%5==0){
                values[idx++] = tmp_value;
                tmp_value = 0;
                cnt = 0;
            }
        }
       
        int dia = picks[0];
        int iron = picks[1];
        int stone = picks[2];

        Integer[] newValues = Arrays.stream(values).boxed().toArray(Integer[]::new);
        Arrays.sort(newValues, (el1, el2) -> el2 -el1);
        System.out.println(Arrays.toString(values));

        for(int i=0; i<newValues.length; i++){
            if (newValues[i] == 0 || (dia ==0 && iron == 0 && stone ==0)){
                break;
            }else{
                if (dia!=0){
                    answer += newValues[i] /31;
                    newValues[i] %= 31;
                    answer += newValues[i]/6;
                    newValues[i] %= 6;
                    answer += newValues[i];
                    dia -= 1;
                } else if(iron!=0){
                    answer += newValues[i] /31 * 5;
                    newValues[i] %= 31;
                    answer += newValues[i]/6;
                    newValues[i] %= 6;
                    answer += newValues[i]/1;
                    iron -= 1;
                } else if(stone!=0) {
                    answer += newValues[i] /31 * 25;
                    newValues[i] %= 31;
                    answer += newValues[i]/6 * 5;
                    newValues[i] %= 6;
                    answer += newValues[i]/1;
                    stone -=1;
                }
            }
        }
        return answer;
    }
}