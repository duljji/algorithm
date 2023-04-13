
import java.util.Scanner;

public class Main {

	public static void main(String[] args) {
		boolean[][] map = new boolean[100][100];
		int answer = 0;
		Scanner sc = new Scanner(System.in);

		for (int i = 0; i < 4; i++) {
			int sy = sc.nextInt();
			int sx = sc.nextInt();
			int ey = sc.nextInt();
			int ex = sc.nextInt();

			for (int j = sx; j < ex; j++) { // 행
				for (int k = sy; k < ey; k++) { // 열
					if ( map[j][k] == false) {
						map[j][k] = true;
						answer++;
					}
				}
			}
		}
		
		System.out.println(answer);
	}
	
}
