class Solution:
    def findUnique(self, arr, n, k):
        res = 0
        for i in range(31):
            sb = 0
            for j in arr:
                if (j >> i) & 1 == 1:
                    sb += 1
            if sb % k != 0:
                res += (1 << i)
        return res
        
        #Code here


#{ 
 # Driver Code Starts
import sys 

if __name__=='__main__':
    T = int(input())

    for _ in range(T):
        n,k=[int(x) for x in input().split()]
        a = [int(x) for x in input().split()]

        print(Solution().findUnique(a,n,k))
# } Driver Code Ends