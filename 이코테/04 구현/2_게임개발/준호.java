import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class 준호 {

    public static int dir;
//    왼쪽으로 도는 메서드 생성
    public static void turn_left() {
        dir -= 1;
        if (dir == -1) {
            dir = 3;
        }
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int M = scanner.nextInt();

        int x = scanner.nextInt();
        int y = scanner.nextInt();
        dir = scanner.nextInt();

        int[][] ints = new int[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                ints[i][j] = scanner.nextInt();
            }
        }
//        2는 방문한 땅
        ints[x][y] = 2;
//        북 동 남 서
        int[] dx = {-1, 0, 1, 0};
        int[] dy = {0, 1, 0, -1};

        int answer = 1;

//        돌아본 횟수
        int count = 0;
        while (true) {
            if (ints[x + dx[dir]][y + dy[dir]] != 0) {
                count++;
                if (count > 4) {
                    turn_left();
                    turn_left();
                    if (ints[x + dx[dir]][y + dy[dir]] == 1) {
                        break;
                    } else {
                        x += dx[dir];
                        y += dy[dir];
                        turn_left();
                        turn_left();
                        count = 0;
                    }
                }else {
                    turn_left();
                }
            } else {
                x += dx[dir];
                y += dy[dir];
                ints[x][y] = 2;
                count = 0;
                answer++;
            }
        }
        System.out.println(answer);
    }
}