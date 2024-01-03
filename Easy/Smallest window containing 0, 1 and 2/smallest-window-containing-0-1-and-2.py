#User function Template for python3
from collections import defaultdict
class Solution:
    def smallestSubstring(self, S):
        mp = defaultdict(int)
        n = len(S)
        ans = float('inf')
        start = 0
        for i in range(n):
            mp[S[i]] += 1
            if len(mp) == 3:
                while start < i and mp[S[start]] > 1:  
                    mp[S[start]] -= 1
                    start += 1
                ans = min(ans, i - start + 1)
        if ans == float('inf'):
            return -1
        return ans
                    
       
        
            
            
            


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
	t=int(input())
	for i in range(t):
		S = input()
		ob = Solution()
		ans = ob.smallestSubstring(S)
		
		print(ans)



# } Driver Code Ends
