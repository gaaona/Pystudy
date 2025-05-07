import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int idx = 0;
        int max_v = 0;
        for (int i = 1; i<10; i++) {
            int num = sc.nextInt();

            if (max_v < num) {
                max_v = num;
                idx = i;
            }
            
        }
        System.out.println(max_v);
        System.out.println(idx);
    }
}