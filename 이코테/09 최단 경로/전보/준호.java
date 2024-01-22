import java.util.*;

//자기 자신과 파라미터로 들어오는 객체를 비교하는 것 - Comparable
class Node implements Comparable<Node> {

    private int index;
    private int distance;

    public Node(int index, int distance) {
        this.index = index;
        this.distance = distance;
    }

    public int getIndex() {
        return this.index;
    }

    public int getDistance() {
        return this.distance;
    }

//거리 가 짧은 것이 높은 우선순위
    @Override
    public int compareTo(Node other) {
        if (this.distance < other.distance) {
            return -1;
        }
        return 1;
    }

}
public class 준호 {

//    무한을 설정
    public static final int INF = (int) 1e9;
    public static int N, M, start;

    public static ArrayList<ArrayList<Node>> graph = new ArrayList<ArrayList<Node>>();

//    최단거리만 기록
    public static int[] d = new int[30001];

    public static void dijkstra(int start) {
        PriorityQueue<Node> pq = new PriorityQueue<>();
        pq.offer(new Node(start, 0));
        d[start] = 0;
        while (!pq.isEmpty()) {
            Node node = pq.poll();
            int dis = node.getDistance();
            int now = node.getIndex();
            if(d[now] < dis) continue;
            for (int i = 0; i < graph.get(now).size(); i++) {
                int cost = d[now] + graph.get(now).get(i).getDistance();
                if (cost < d[graph.get(now).get(i).getIndex()]) {
                    d[graph.get(now).get(i).getIndex()] = cost;
                    pq.offer(new Node(graph.get(now).get(i).getIndex(), cost));
                }
            }
        }
    }
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        N = scanner.nextInt();
        M = scanner.nextInt();
        start = scanner.nextInt();

        for (int i = 0; i <= N; i++) {
            graph.add(new ArrayList<Node>());
        }

        for (int i = 0; i < M; i++) {
            int a = scanner.nextInt();
            int b = scanner.nextInt();
            int c = scanner.nextInt();

            graph.get(a).add(new Node(b, c));
        }

        Arrays.fill(d, INF);

        dijkstra(start);

        int max = 0;
        int count = 0;
        for (int i = 1; i <= N; i++) {
            if (d[i] < INF) {
                count++;
                max = Math.max(d[i], max);
            }
        }
//        본인 제외
        count--;
        System.out.print(count + " " + max);
    }
}
