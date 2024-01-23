import java.util.*;

public class 준호 {
    public static int N ,M;
    public static int[] parent = new int[100001];

    public static int findParent(int x) {
        if(parent[x] == x) return x;
        return parent[x] = findParent(parent[x]);
    }

    public static void unionParent(int a, int b) {
        a = findParent(a);
        b = findParent(b);
        if (a > b) {
            parent[a] = b;
        } else {
            parent[b] = a;
        }
    }

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        N = scanner.nextInt();
        M = scanner.nextInt();

        for (int i = 0; i <= N; i++) {
            parent[i] = i;
        }

        StringBuilder result = new StringBuilder();
        for (int i = 0; i < M; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            int c = scanner.nextInt();
            if (a == 1) {
                if (findParent(b) == findParent(c)) {
                    result.append("YES ");
                } else {
                    result.append("NO ");
                }
            } else {
                unionParent(b, c);
            }
        }
        System.out.println(result);
    }
}
