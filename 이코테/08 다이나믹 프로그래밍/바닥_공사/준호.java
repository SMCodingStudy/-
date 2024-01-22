import java.util.Scanner;

public class 준호 {
    public static void main(String[] args) {

//        바닥공사
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();

        int[] count = new int[N];
        count[0] = 1;
        count[1] = 3;
        for (int i = 2; i < N; i++) {
            count[i] = count[i - 1] + count[i - 2] * 2;
        }
        System.out.println(count[N - 1]);
    }
}
