import java.util.*;

public class 준호 {
    public static final int INF = (int) 1e9;
    public static int N, M, X, K;
    public static int[][] graph = new int[101][101];

    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        N = scanner.nextInt();
        M = scanner.nextInt();
        for (int i = 0; i < 101; i++) {
            Arrays.fill(graph[i], INF);
        }
        for (int a = 1; a <= N; a++) {
            for (int b = 1; b <= N; b++) {
                if (a == b) {
                    graph[a][b] = 0;
                }
            }
        }

        for (int i = 0; i < M; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            graph[a][b] = 1;
            graph[b][a] = 1;
        }

        X = scanner.nextInt();
        K = scanner.nextInt();

        for (int i = 1; i <= N; i++) {
            for (int j = 1; j <= N; j++) {
                for (int k = 1; k <= N; k++) {
                    graph[i][j] = Math.min(graph[i][j], graph[i][k] + graph[k][j]);
                }
            }
        }
        int distance = graph[1][K] + graph[K][X];

        if (distance >= INF) {
            System.out.println(-1);
        } else {
            System.out.println(distance);
        }
    }

}
