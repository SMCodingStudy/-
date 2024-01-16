import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class 준호 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        scanner.nextLine();
        String[] plans = scanner.nextLine().split(" ");

//        L, R, U, D 순서로 배열 생성
        int[] moveX = {-1, 1, 0, 0};
        int[] moveY = {0, 0, -1, 1};
        char[] moveTypes = {'L', 'R', 'U', 'D'};

        int[] now = {1, 1};

        for (int i = 0; i < plans.length; i++) {
            char c = plans[i].charAt(0);
            int a = -1;
            int b = -1;
            for (int j = 0; j < moveTypes.length; j++) {
                if (c == moveTypes[j]) {
                    a = now[0] + moveY[j];
                    b = now[1] + moveX[j];
                }
            }
            if (a > N || b > N || a < 1 || b < 1) continue;

            now[0] = a;
            now[1] = b;
        }
        System.out.println(now[0] + ", " + now[1]);
    }
}