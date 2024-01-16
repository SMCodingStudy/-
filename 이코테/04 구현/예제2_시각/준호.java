import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class 준호 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();

        int count = 0;

        for (int i = 0; i <= N; i++) {
            for (int j = 0; j < 60; j++) {
                for (int k = 0; k < 60; k++) {
                    if (k / 10 == 3 || k % 10 == 3) {
                        count++;
                    } else if (j / 10 == 3 || j % 10 == 3) {
                        count++;
                    } else if (i % 10 == 3) {
                        count++;
                    }
                }
            }
        }
        System.out.println(count);
    }
}