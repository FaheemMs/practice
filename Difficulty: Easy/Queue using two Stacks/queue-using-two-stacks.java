//{ Driver Code Starts
import java.util.*;
import java.util.Stack;
import java.util.LinkedList;



class GfG
{
	public static void main(String args[])
	{
	    //Taking input using class Scanner
		Scanner sc = new Scanner(System.in);
		
		//Taking input the number of testcases
		int t = sc.nextInt();
		while(t>0)
		{
		    //Creating a new object of class StackQueue
			StackQueue g = new StackQueue();
			
			//Taking input the total number of Queries
			int q = sc.nextInt();
			while(q>0)
			{
				int QueryTyoe = sc.nextInt();
				
				//If QueryTyoe is 1 then
				//we call the Push method
				//of class StackQueue
				//else we call the Pop method
				if(QueryTyoe == 1)
				{
					int a = sc.nextInt();
					g.Push(a);
				}else
				if(QueryTyoe == 2)
				System.out.print(g.Pop()+" ");
			q--;
				
			}
			System.out.println();
		t--;
		}
	}
}


// } Driver Code Ends


class StackQueue
{
    Stack<Integer> input = new Stack<Integer>();
    Stack<Integer> output = new Stack<Integer>();

    //Function to push an element in queue by using 2 stacks.
    void Push(int x)
    {
	   // Your code here
	   input.push(x);
    }
	
    
    //Function to pop an element from queue by using 2 stacks.
    int Pop()
    {
	   // Your code here
	   while(input.size() > 1){
	        output.push(input.pop());
	    }
	    if(input.size() > 0){
    	    int x = input.pop();
    	    while(output.size() > 0){
    	        input.push(output.pop());
    	        
    	    }
    	    return x;
	    }
	    return -1;
	    
    }
}
