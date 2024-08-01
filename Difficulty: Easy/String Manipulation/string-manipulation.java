//{ Driver Code Starts
import java.util.*;
import java.lang.*;
import java.io.*;

class GFG
{
	public static void main(String[] args) throws IOException
	{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine().trim());
        while(t-->0)
        {
            int n = Integer.parseInt(br.readLine().trim());
            String inputLine[] = br.readLine().trim().split(" ");
            Vector<String> v = new Vector<>(); 
            for (int i = 0; i < n; i++) {
                v.addElement(inputLine[i]);
            }
            
            Solution obj = new Solution();
            System.out.println(obj.removeConsecutiveSame(v));
            
        }
	}
}


// } Driver Code Ends



class Solution 
{
      
    static int removeConsecutiveSame(Vector <String > v) 
    {
        // Your code goes here
        ArrayList<String> al = new ArrayList<>();
        al.add(v.get(0));
        //int pos = 0;
        for(int i = 1; i < v.size(); i++){
            if(al.size() > 0 && v.get(i).equals(al.get(al.size() - 1))){
                al.remove(al.size() - 1);
            }
            else{
                al.add(v.get(i));
            }
        }
        return al.size();
    }
}