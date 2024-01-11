#User function Template for python3

class Solution:

    def removeKdigits(self, s, k):
        # code here
        res = []
        for i in s:
            while len(res) > 0 and res[-1] > i and k:
                res.pop()
                k -= 1
            if len(res) > 0 or i != '0':
                res.append(i)
        while len(res) > 0 and  k:
            res.pop()
            k -= 1
        st = "".join(res)
        if st == "":
            return '0'
        return st


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':

    t = int(input())

    for _ in range(t):
        S = input()
        K = int(input())

        obj = Solution()

        ans = obj.removeKdigits(S, K)

        print(ans)


# } Driver Code Ends