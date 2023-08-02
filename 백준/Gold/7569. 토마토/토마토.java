import java.util.*;
import java.io.*;

public class Main {
    private static int R, C, H;

    static class Tomato{
        int r;
        int c;
        int h;

        int depth;

        Tomato(int h, int r, int c, int depth){
            this.r = r;
            this.c = c;
            this.h = h;
            this.depth = depth;
        }
    }

    static int[] dr = {-1, 1, 0, 0};
    static int[] dc = {0, 0, -1, 1};


    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine(), " ");

        C = Integer.parseInt(st.nextToken());
        R = Integer.parseInt(st.nextToken());
        H = Integer.parseInt(st.nextToken());
        int[][][] box = new int[H][R][C];
        Queue<Tomato> q = new LinkedList<>();
        for (int h = 0; h < H; h++) {
            for (int i = 0; i < R; i++) {
                st = new StringTokenizer(br.readLine(), " ");
                for (int j = 0; j < C; j++) {
                    int num = Integer.valueOf(st.nextToken());
                    box[h][i][j] = Integer.valueOf(num);
                    if(num == 1){
                        q.add(new Tomato(h, i, j, 0));
                    }

                }
            }
        }
        int answer = 0;
        while(!q.isEmpty()){
            Tomato t = q.poll();
            //같은 박스에 있는 토마토 익게 만들기
            for(int d = 0; d<4; d++){
                int nr = t.r + dr[d];
                int nc = t.c + dc[d];
                if(nr < 0 || nr >= R || nc < 0 || nc >= C) continue;

                if(box[t.h][nr][nc] == 0){
                    box[t.h][nr][nc] = 1;
                    q.add(new Tomato(t.h, nr, nc, t.depth+1));
                }
            }
            if(t.h + 1 < H && box[t.h+1][t.r][t.c] == 0){
                box[t.h+1][t.r][t.c] = 1;
                q.add(new Tomato(t.h+1, t.r, t.c, t.depth+1));
            }
            if(t.h - 1 >= 0 && box[t.h-1][t.r][t.c] == 0){
                box[t.h-1][t.r][t.c] = 1;
                q.add(new Tomato(t.h-1, t.r, t.c, t.depth+1));
            }
            if(q.isEmpty()){
                answer = t.depth;
            }
        }
        for (int h = 0; h < H; h++) {
            for (int i = 0; i < R; i++) {
                for (int j = 0; j < C; j++) {
                    if(box[h][i][j] == 0){
                        answer = -1;
                        break;
                    }
                }
            }
        }
        System.out.println(answer);

    }
}