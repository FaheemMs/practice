#User function Template for python3

class Solution:
    def splitArray(self, arr, N, k):
        ans = float('inf')
        def checker(max_sum):
            cuts = 1
            summ = 0
            for i in range(N):
                if summ + arr[i] > max_sum:
                    cuts += 1
                    summ = arr[i]
                else:
                    summ += arr[i]
            #print("cuts", cuts)
            return cuts <= k
        low = max(arr)
        high = sum(arr)
        while low <= high:
            mid = low + (high - low) // 2
            x = checker(mid)
            if x :
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1
        return ans
            

#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N,K=map(int,input().split())
        arr=list(map(int,input().split()))
        
        ob = Solution()
        print(ob.splitArray(arr,N,K))
# } Driver Code Ends