import java.util.*;

public class 준호 {
    public static int N;

    public static int binarySearch(int[] total, int M) {
        int start = 0;
        int end = total[N - 1];
        int result = 0;
        while (start <= end) {
            int mid = (start + end) / 2;
            int ans = 0;
            for (int i = 0; i < N; i++) {
                if (total[i] > mid) {
                    ans += total[i] - mid;
                }
            }
            if (ans < M) {
                end = mid - 1;
            } else {
                result = mid;
                start = mid + 1;
            }
        }
        return result;
    }

    /*
    //이진 탐색 소스코드 구현(반복문)
    public static int binarySearch(int[] arr, int target, int start, int end) {
        while (start <= end) {
            int mid = (start + end) / 2;
            // 찾은 경우 중간점 인덱스 반환
            if (arr[mid] == target) return mid;
            // 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
            else if (arr[mid] > target) end = mid - 1;
            // 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
            else start = mid + 1;
        }
        return -1;
    }*/

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        N = scanner.nextInt();
        int M = scanner.nextInt();
        int[] total = new int[N];
        for (int i = 0; i < N; i++) {
            total[i] = scanner.nextInt();
        }
        int answer = binarySearch(total, M);
        System.out.println(answer);
    }
}