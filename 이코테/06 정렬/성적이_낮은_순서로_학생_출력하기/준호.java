import java.util.*;

public class 준호 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int N = scanner.nextInt();
        scanner.nextLine();
        String[][] examples = new String[N][2];
        for (int i = 0; i < N; i++) {
            String[] split = scanner.nextLine().split(" ");
            examples[i][0] = split[0];
            examples[i][1] = split[1];
        }
        Arrays.sort(examples, Comparator.comparingInt(o -> Integer.parseInt(o[1])));

        for (int i = 0; i < N; i++) {
            System.out.print(examples[i][0] + " ");
        }
    }
}