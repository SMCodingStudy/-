import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class 준호 {

    public static int N,M;
    public static int[][] a = new int[1000][1000];

//DFS 메서드
    public static boolean cal(int x, int y) {
        if (x <= -1 || y <= -1 || x >= N || y >= M) {
            return false;
        }
        if (a[x][y] == 0) {
            a[x][y] = 1;
            cal(x + 1, y);
            cal(x, y + 1);
            return true;
        }
        return false;
    }

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        N = scanner.nextInt();
        M = scanner.nextInt();
        scanner.nextLine();
        int answer = 0;
        for (int i = 0; i < N; i++) {
            String s = scanner.nextLine();
            for (int j = 0; j < M; j++) {
                a[i][j] = s.charAt(j) - '0';
            }
        }

//        for문 돌아가면서 DFS메서드 실행
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                if (cal(i, j)) {
                    answer++;
                }
            }
        }
        System.out.println(answer);
    }
}