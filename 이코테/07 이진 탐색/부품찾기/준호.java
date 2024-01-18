import java.util.*;

public class 준호 {

    public static int binarySearch(int[] total, int target, int start, int end) {

        if (start > end) {
            return -1;
        }
        int mid = (start + end) / 2;

        if (total[mid] == target) {
            return mid;
        } else if (total[mid] > target) {
            return binarySearch(total, target, start, mid - 1);
        } else return binarySearch(total, target, mid + 1, end);
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
        int N = scanner.nextInt();
        scanner.nextLine();
        int[] total = new int[N];
        for (int i = 0; i < N; i++) {
            total[i] = scanner.nextInt();
        }
        scanner.nextLine();
        int M = scanner.nextInt();
        int[] order = new int[M];
        for (int i = 0; i < M; i++) {
            order[i] = scanner.nextInt();
        }

        Arrays.sort(total);

        for (int i = 0; i < M; i++) {
            int a = binarySearch(total, order[i], 0, N - 1);
            if (a == -1) {
                System.out.print("no ");
            } else {
                System.out.print("yes ");
            }
        }
    }
}