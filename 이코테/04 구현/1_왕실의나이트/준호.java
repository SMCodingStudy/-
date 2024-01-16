import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class 준호 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        String input = scanner.next();
        String[] split = input.split("");
        int answer = 0;

//        입력값을 좌표로 변경
        int dx = Integer.parseInt(split[1]);
        int dy = (int) split[0].charAt(0) - 'a' + 1;

//        경우의 수 미리 배열
        int[][] step = {{-2, -1}, {-2, 1}, {-1, -2},
                {1, -2}, {2, 1}, {2, -1}, {-1, 2}, {1, 2}};

//        지정된 판을 벗어나는 경우 제외
        for (int i = 0; i < step.length; i++) {
            if (dy + step[i][0] > 0 && dx + step[i][1] > 0) {
                answer++;
            }
        }
        System.out.println(answer);

    }
}