class Solution:
	def longSubarrWthSumDivByK (self,arr,  n, k) : 
		#Complete the function
		mp = {}
		mp[0] = -1
		summ = 0
		maxlen = 0
		for i in range(n):
		    summ += arr[i]
		    rem = summ % k
		    if rem < 0:
		        rem += k
		    if rem not in mp:
		        mp[rem] = i
		    else:
		        maxlen = max(maxlen, i - mp[rem])
		return maxlen



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

	for _ in range(0,int(input())):
		n, K = map(int ,input().split())
		arr = list(map(int,input().strip().split()))
		ob = Solution()
		res = ob.longSubarrWthSumDivByK(arr, n, K)
		print(res)




# } Driver Code Ends