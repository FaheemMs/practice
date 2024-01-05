#User function Template for python3
class Solution:

	def fascinating(self,n):
	    by2 = n * 2
	    by3 = n * 3
	    x = str(n) + str(by2)+ str(by3)
	    return list(map(int, sorted(list(x)))) == list(range(1, 10))
	    # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3



if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n = int(input().strip())
        ob = Solution()
        ans = ob.fascinating(n)
        if ans:
            print("Fascinating")
        else:
            print("Not Fascinating")
        tc -= 1

# } Driver Code Ends