import java.util.Arrays;
import java.util.Scanner;

class Main{
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        int N = sc.nextInt();
        int[] alphabet = new int[26];

        while(N-- > 0){
            char[] word = sc.next().toCharArray();
            int placeValue = 1;

            for (int i = word.length - 1; i >= 0; i--){
                alphabet[word[i]-'A'] = alphabet[word[i]-'A'] + placeValue;
                placeValue *= 10;
            }

        }
        Arrays.sort(alphabet);

        int ans = 0;
        for (int i = 0; i < 10; i++){
            ans = ans + alphabet[25-i] * (9 - i);
        }
        System.out.println(ans);
    }
}