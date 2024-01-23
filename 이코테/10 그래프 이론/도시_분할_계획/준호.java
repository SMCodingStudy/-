import java.util.*;
    class Edge implements Comparable<Edge> {
        private int distance;
        private int nodeA;
        private int nodeB;

        public Edge(int distance, int nodeA, int nodeB) {
            this.distance = distance;
            this.nodeA = nodeA;
            this.nodeB = nodeB;
        }

        public int getDistance() {
            return this.distance;
        }

        public int getNodeA() {
            return this.nodeA;
        }

        public int getNodeB() {
            return this.nodeB;
        }

        @Override
        public int compareTo(Edge other) {
            if (this.distance < other.distance) {
                return -1;
            }
            return 1;
        }
    }

    public class 도시_분할_계획 {
        public static int N, M;
        public static int[] parent = new int[100001];
        public static ArrayList<Edge> edges = new ArrayList<>();
        public static int result = 0;

        public static int findParent(int x) {
            if (x == parent[x]) return x;
            return parent[x] = findParent(parent[x]);
        }

        public static void unionParent(int a, int b) {
            a = findParent(a);
            b = findParent(b);
            if (a < b) parent[b] = a;
            else parent[a] = b;
        }

        public static void main(String[] args) {
            Scanner scanner = new Scanner(System.in);
            N = scanner.nextInt();
            M = scanner.nextInt();

            for (int i = 0; i <= N; i++) {
                parent[i] = i;
            }

            for (int i = 0; i < M; i++) {
                int a = scanner.nextInt();
                int b = scanner.nextInt();
                int cost = scanner.nextInt();
                edges.add(new Edge(cost, a, b));
            }

            Collections.sort(edges);
            int max = 0;

            for (Edge edge : edges) {
                int cost = edge.getDistance();
                int a = edge.getNodeA();
                int b = edge.getNodeB();
                if (findParent(a) != findParent(b)) {
                    unionParent(a, b);
                    result += cost;
                    max = cost;
                }
            }
            System.out.println(result - max);
//            한 마을의 임의의 두 집을 이은 길이 없는 경우인데 ?
        }
}
