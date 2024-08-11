//{ Driver Code Starts
import java.io.*;
import java.util.*;

class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t;
        t = Integer.parseInt(br.readLine());
        while(t-- > 0){
            
            String s; 
            s = br.readLine();
            
            Solution obj = new Solution();
            String res = obj.removePair(s);
            
            System.out.println(res);
            
        }
    }
}

// } Driver Code Ends


class Solution {
    public static String removePair(String s) {
        // code here
        Stack<Character> stk =  new Stack<>();
        for(int i = 0; i <= s.length(); i++){
            if(stk.size() >= 2){
                char ch1 = stk.pop();
                char ch2 = stk.pop();
                if(ch1 != ch2){
                    stk.push(ch2);
                    stk.push(ch1);
                }
            }
            if(i < s.length()){
            char ch = s.charAt(i);
            stk.push(ch);
        }
        }
        
        String res = "";
        while(stk.size() > 0){
            res = stk.pop() + res;
        }
        if(res == "") return "-1";
        return res;
    }
}
        
