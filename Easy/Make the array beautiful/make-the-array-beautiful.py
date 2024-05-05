#User function Template for python3

from typing import List

class Solution:
    def makeBeautiful(self, arr: List[int]) -> List[int]:
        if len(arr) <= 1:
            return arr
        res = []
        for i in range(len(arr)):
            if len(res) == 0:
                res.append(arr[i])
            elif (res[-1] >= 0 and arr[i] < 0 ) or (res[-1] < 0 and arr[i] >= 0):
                res.pop()
            else:
                res.append(arr[i])
        return res
        # code here


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        n = int(input())
        
        arr = list(map(int,input().split()))
        
        obj = Solution()
        res = obj.makeBeautiful(arr)
        print(*res)
# } Driver Code Ends