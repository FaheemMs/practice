class Solution:
    def transitionPoint(self, arr, n):
        l = 0
        h = n -1
        ans = -1
        while l <= h:
            mid = (l+h) // 2
            if arr[mid] == 0:
                l += 1
            else:
                ans = mid
                h -= 1
        return ans
        # Code here


#{ 
 # Driver Code Starts
#driver code
if __name__=='__main__':
    t=int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        ob = Solution()
        print(ob.transitionPoint(arr, n))

# } Driver Code Ends