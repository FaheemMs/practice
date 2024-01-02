# User function Template for python3

class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        pre_sum = [0] * N
        suff_sum = [0]*N
        pre_sum[0] = A[0]
        suff_sum[N-1] = A[N-1]
        for i in range(1, N):
            pre_sum[i] = A[i] + pre_sum[i-1]
            suff_sum[N-i-1] = suff_sum[N-i] + A[N-i-1]
        for i in range(N):
            if pre_sum[i] == suff_sum[i]:
                return i+1
        return -1
        # Your code here



#{ 
 # Driver Code Starts
# Initial Template for Python 3

import math


def main():

    T = int(input())

    while(T > 0):

        N = int(input())

        A = [int(x) for x in input().strip().split()]
        ob=Solution()

        print(ob.equilibriumPoint(A, N))

        T -= 1


if __name__ == "__main__":
    main()

# } Driver Code Ends