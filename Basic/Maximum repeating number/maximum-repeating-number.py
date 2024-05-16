#User function Template for python3
class Solution:

    def maxRepeating(self,arr, n, k):
        cnt = [0] * k
        maxi = 0
        ans = None
        for i in range(n):
            cnt[arr[i]] += 1
        for i in range(k):
            if cnt[i] > maxi:
                ans = i
                maxi = cnt[i]
        return ans
        # code here





#{ 
 # Driver Code Starts
#Initial Template for Python 3





if __name__ == '__main__':
    tc = int(input())
    while tc > 0:
        n, k = list(map(int, input().strip().split()))
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        ans = ob.maxRepeating(arr, n, k)
        print(ans)
        tc -= 1


# } Driver Code Ends