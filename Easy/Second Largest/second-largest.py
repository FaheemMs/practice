#User function Template for python3
class Solution:
	def print2largest(self,arr, n):
	    if n == 1:
	        return -1
	    sec_maxi = -1
	    maxi = arr[0]
	    for i in range(n):
	        if arr[i] > maxi:
	            sec_maxi = maxi
	            maxi = arr[i]
	        elif arr[i] != maxi and arr[i] > sec_maxi:
	            sec_maxi = arr[i]
	    return sec_maxi
		# code here


#{ 
 # Driver Code Starts
# Initial Template for Python 3
if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.print2largest(arr, n)
        print(ans)
        tc -= 1

# } Driver Code Ends