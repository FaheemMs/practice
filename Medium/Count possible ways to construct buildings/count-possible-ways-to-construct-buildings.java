//{ Driver Code Starts
//Initial Template for Java

import java.util.*;
import java.lang.*;
import java.io.*;
class GFG
{
    public static void main(String[] args) throws IOException
    {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int T = Integer.parseInt(br.readLine().trim());
        while(T-->0)
        {
            int N = Integer.parseInt(br.readLine().trim());
            Solution ob = new Solution();
            int ans = ob.TotalWays(N);
            System.out.println(ans);           
        }
    }
}

// } Driver Code Ends




//User function Template for Java

class Solution
{
    public int TotalWays(int N)
    {
        long M = 1000000007;
        long[] fib = new long[N];
        fib[0] = 2;
        if(N == 1){
            return 4;
        }
        fib[1] = 3;
        for(int i = 2; i < N; i++){
            fib[i] = (fib[i-1] % M + fib[i-2] % M) % M;
        }
        long ans = fib[N-1];
        ans = ((ans % M) * (ans % M)) % M;
        return (int)ans;
       
    }

}