
from collections import defaultdict
import math
from typing import List
class Solution:
    def sumOfPowers(self, a : int, b : int) -> int:
        mp = defaultdict(int)
        sm_pf = [k for k in range(b + 1)] #smallest_primefator
        ans = 0
        def seive():
            for i in range(2, b + 1, 2):
                sm_pf[i] = 2
            for i in range(3, int((b + 1) ** 0.5) + 1):
                if sm_pf[i] == i:
                    for j in range(i, b + 1, i):
                        sm_pf[j] = i
                        
        def prime_factorize(n):
            while n != 1:
                mp[sm_pf[n]] += 1
                n //= sm_pf[n]
        seive()
        for i in range(a, b+1):
            prime_factorize(i)
        return sum(mp.values())
        # code here
        






#{ 
 # Driver Code Starts

class IntArray:
    def __init__(self) -> None:
        pass
    def Input(self,n):
        arr=[int(i) for i in input().strip().split()]#array input
        return arr
    def Print(self,arr):
        for i in arr:
            print(i,end=" ")
        print()


if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a=int(input())
        b=int(input())
        
        obj = Solution()
        res = obj.sumOfPowers(a,b)
        
        print(res)
        

# } Driver Code Ends