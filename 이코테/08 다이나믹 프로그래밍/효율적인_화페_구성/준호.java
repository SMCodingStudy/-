import java.util.Arrays;
import java.util.Scanner;

public class 준호 {
    public static void main(String[] args) {
//        효율적인 화폐 구성
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int M = scanner.nextInt();
        int[] number = new int[N];
        for (int i = 0; i < N; i++) {
            number[i] = scanner.nextInt();
        }

        int[] total = new int[M+1];
        Arrays.fill(total, 10001);

        total[0] = 0;
        for (int i = 0; i < N; i++) {
            for (int j = number[i]; j <= M; j++) {
                if (total[j - number[i]] != 10001) {
                    total[j] = Math.min(total[j], total[j - number[i]] + 1);
                }
            }
        }
        if (total[M] != 10001) {
            System.out.println(total[M]);
        } else {
            System.out.println(-1);
        }
    }
}
