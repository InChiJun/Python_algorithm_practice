package Exam;
import java.io.IOException;
import java.util.Scanner;

public class exam005 { //교재의 슈도코드를 보고 작성하였습니다.
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        int N = sc.nextInt();
        int M = sc.nextInt();
        int[] S = new int[N];
        int[] C = new int[10]; //나머지 카운트 셀 배열

        S[0] = sc.nextInt();
        for(int i = 1; i < N; i++){
            S[i] = sc.nextInt();
            S[i] += S[i-1]; //합배열
        }

        int count = 0;
        int remainer = 0;
        for(int i = 0; i < N; i++){
            remainer = S[i] % M;
            if(remainer == 0) count++;
            C[remainer]++;
        }
        for(int i = 0; i < 10; i++) if(C[i] != 0) count += C[i] * (C[i] - 1) / 2;
        System.out.println(count);
    }
}