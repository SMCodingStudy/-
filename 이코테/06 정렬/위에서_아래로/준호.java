import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class 준호 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        Integer[] examples = new Integer[N];
        for (int i = 0; i < N; i++) {
            examples[i] = scanner.nextInt();
        }
        Arrays.sort(examples, Collections.reverseOrder());

        System.out.println(Arrays.toString(examples));
    }
}