package Exam;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Scanner;
import java.util.StringTokenizer;

public class exam004 {
    public static void main(String[] args) throws IOException {
        Scanner sc = new Scanner(System.in);
        BufferedReader bf = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(bf.readLine());
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int[][] arr = new int[N+1][N+1];
        int[][] S = new int[N+1][N+1];
        for(int i = 1; i < N; i++){ //2차원 배열 생성
            for(int j = 1; j < N; j++){
                arr[i][j] = sc.nextInt();
                S[i][j] = S[i-1][j] + S[i][j-1] + arr[i][j] - S[i-1][j-1];
            }
        }

        st = new StringTokenizer(bf.readLine());
        int[] askArr = new int[4];
        for(int i = 0; i < M; i++){
            for(int j = 0; j < 4; j++) askArr[j] = Integer.parseInt(st.nextToken());
            System.out.println(S[askArr[2]][askArr[3]] - S[askArr[0]-1][askArr[1]] - S[askArr[0]][askArr[1]-1] + S[askArr[0]-1][askArr[1]-1]);
        }

    }
}