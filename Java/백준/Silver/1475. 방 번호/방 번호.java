import java.util.Scanner;

class Main{
    public static void main(String[] args){
        Scanner sc = new Scanner(System.in);
        int max = 0;
        int[] set = new int[10];
        char[] nums = sc.nextLine().toCharArray();

        for (char num : nums){
            set[(num - '0')]++;
        }

        for (int i = 0; i < 9 ; i++){
            if (i != 6){
                max = Math.max(set[i], max);
            }
        }

        if ((set[6] + set[9]+1)/2 > max) {
            System.out.println((set[6] + set[9]+1)/2);
        }else{
            System.out.println(max);
        }
    }


}