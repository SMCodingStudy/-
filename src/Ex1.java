import java.util.Arrays;
import java.util.Scanner;

public class Ex1 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        int N = scanner.nextInt();
        int K = scanner.nextInt();

        int[] A = new int[N];
        int[] B = new int[N];
        for (int i = 0; i < N; i++) {
            A[i] = scanner.nextInt();
        }
        for (int i = 0; i < N; i++) {
            B[i] = scanner.nextInt();
        }

        int answer = 0;

        Arrays.sort(A);
        Arrays.sort(B);

        for (int i = 0; i < K; i++) {
            int temp = A[i];
            A[i] = B[N - i - 1];
            B[N - i - 1] = temp;
//            정렬후 교환한 A[i] 보다 A[i+1]이 같거나 크면 더 교환할 이유가 없음.
            if (A[i] <= A[i + 1]) {
                break;
            }
        }


        for (int i = 0; i < N; i++) {
            answer += A[i];
        }
        System.out.println(answer);
    }
}
