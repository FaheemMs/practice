//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String args[]) throws IOException {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        while (t > 0) {
            int N = sc.nextInt();
            int M[][] = new int[N][N];
            for (int i = 0; i < N; i++) {
                for (int j = 0; j < N; j++) {
                    M[i][j] = sc.nextInt();
                }
            }
            System.out.println(new Solution().celebrity(M));
            t--;
        }
    }
}
// } Driver Code Ends


// User function Template for Java

class Solution {
    // Function to find if there is a celebrity in the party or not.
    public int celebrity(int mat[][]) {
        // code here
        Stack<Integer> stk = new Stack<>();
        int n = mat.length;
        for(int i = 0; i < n; i++){
            stk.push(i);
        }
        while(stk.size() >= 2){
            int mem1 = stk.pop();
            int mem2 = stk.pop();
            if(mat[mem1][mem2] == 1)
                stk.push(mem2);
            else
                stk.push(mem1);
        }
        if(stk.size() == 0)
            return -1;
        int potential =  stk.pop();
        for(int i = 0; i < n; i++){
            if(i != potential)
            if(mat[potential][i] == 1 || mat[i][potential] == 0)
                return -1;
        }
        return potential;
    }
}