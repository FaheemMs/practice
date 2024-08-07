//{ Driver Code Starts
// Initial template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();

        while (t-- > 0) {
            int sizeOfStack = sc.nextInt();
            Stack<Integer> myStack = new Stack<>();

            // adding elements to the stack
            for (int i = 0; i < sizeOfStack; i++) {
                int x = sc.nextInt();
                myStack.push(x);
            }
            Solution obj = new Solution();
            obj.deleteMid(myStack, sizeOfStack);

            while (!myStack.isEmpty()) {
                System.out.print(myStack.peek() + " ");
                myStack.pop();
            }
            System.out.println();
        }
    }
}
// } Driver Code Ends


// User function Template for Java

class Solution {
    // Function to delete middle element of a stack.
    public Stack<Integer> delMid(Stack<Integer> stk, int currSize, int size){
        if((size % 2 == 1 && currSize == size / 2 + 1) || (size % 2 == 0 && currSize == size / 2)){
            stk.pop();
            return stk;
        }
        int ele = stk.peek();
        stk.pop();
        stk = delMid(stk, stk.size(), size);
        stk.push(ele);
        return stk;
    }
    public void deleteMid(Stack<Integer> s, int sizeOfStack) {
        // code here
        s = delMid(s, s.size(), s.size());
        
    }
}
