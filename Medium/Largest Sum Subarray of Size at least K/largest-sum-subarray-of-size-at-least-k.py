#User function Template for python3

class Solution():
    def maxSumWithK(self, arr, n, k):
        # Code here
        i,j = 0,0
        summ = last = 0
        maxi = -float('inf')
        while j < n:
            summ += arr[j]
            if (j-i+1) == k:
                maxi = max(maxi, summ)
            elif (j-i+1) > k:
                last += arr[i]
                i += 1
                if last < 0:
                    summ -= last
                    last = 0
                maxi = max(maxi, summ)
            j += 1
        return maxi
                    
    
    
    


#{ 
 # Driver Code Starts
#Initial Template for Python 3

def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        k = int(input())
        
        ob = Solution()
        print(ob.maxSumWithK(a, n, k))

        T -= 1


if __name__ == "__main__":
    main()


# } Driver Code Ends