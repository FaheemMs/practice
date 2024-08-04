//{ Driver Code Starts
//Initial Template for Java

import java.io.*;
import java.util.*;

class GFG
{
    public static void main(String args[])throws IOException
    {
        BufferedReader in=new BufferedReader(new InputStreamReader(System.in));
        PrintWriter out=new PrintWriter(System.out);
        int t = Integer.parseInt(in.readLine().trim());
        while(t-- > 0)
        {
            String s;
            s = in.readLine().trim();
            
            Solution ob = new Solution();
            
            out.println(ob.reverseEqn(s));    
        }
        out.close();
    }
}
// } Driver Code Ends


//User function Template for Java
class Solution
{
   
    String reverseEqn(String S)
    {
        // your code here
        Stack<String> stk = new Stack<>();
        for(int i = 0; i < S.length(); ){
            char ch = S.charAt(i);
            String num = "";
            while(i < S.length() && Character.isDigit(S.charAt(i))){
                num += S.charAt(i);
                i += 1;
            }

            if(num != "")
                stk.push(num);
            else{
                stk.push(ch+"");
                i++;
            }
            
        }
        StringBuilder res = new StringBuilder("");
        while(stk.size() > 0){
            res.append(stk.pop());
        }
        return res + "";
    }
}