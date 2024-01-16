import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class 준호 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int K = scanner.nextInt();

        int count = 0;
        while (N >= K) {
            if (N % K > 0) {
                count += N % K;
            }
            N = N / K;
            count++;
        }

        System.out.println(count);
    }
}