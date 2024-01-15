import java.util.Arrays;
import java.util.Collections;
import java.util.Scanner;

public class 준호 {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        int M = scanner.nextInt();

        Integer[][] arr = new Integer[N][M];
        for (int i = 0; i < N; i++) {
            for (int j = 0; j < M; j++) {
                arr[i][j] = scanner.nextInt();
            }
        }
//        각 행마다 가장 작은 값을 배열로 저장
        Integer[] count = new Integer[N];
        for (int i = 0; i < N; i++) {
            Arrays.sort(arr[i]);
            count[i] = arr[i][0];
        }
//        저장한 배열을 오름차순으로 정렬 후 가장 큰 값 출력
        Arrays.sort(count);
        int answer = count[N - 1];
        System.out.println(answer);
        // 문제를 푼 후 모범답안을 확인해봤는데 입력과 동시에 열에서의 최소값을 저장하고,
        // 행에서의 최대값을 저장하여 입력이 끝나는 동시에 출력이 되도록하는 방법이 효율적인 것을 확인함
    }
}
