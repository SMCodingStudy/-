import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class 준호 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int M = scanner.nextInt();
        int K = scanner.nextInt();

        Integer[] arr = new Integer[N];
        for (int i = 0; i < N; i++) {
            arr[i] = scanner.nextInt();
        }

//        입력받은 배열 내림차순 정렬
        Arrays.sort(arr, Collections.reverseOrder());

//        가장 큰 값과 두번째로 큰 값
        int first = arr[0];
        int second = arr[1];

//        가장 큰 값의 개수
        int count = (M / (K + 1)) * K + M % (K + 1);
        int answer = count * first + (M - count) * second;
        System.out.println(answer);
    }
}