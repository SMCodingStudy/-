import java.util.Scanner;

public class Test {
    public static void main(String[] args) {
//        개미전사

        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int[] K = new int[N];
        int[] total = new int[N];
        for (int i = 0; i < N; i++) {
            K[i] = scanner.nextInt();
            total[i] = 0;
        }
        total[0] = K[0];
        total[1] = Math.max(K[0], K[1]);

        for (int i = 2; i < N; i++) {
            int a = total[i - 2] + K[i];
            total[i] = Math.max(a, total[i - 1]);
        }
        System.out.println(total[N-1]);
    }
}
