

from typing import List
class Solution:
    def is_possible_to_get_seats(self, n : int, m : int, arr : List[int]) -> bool:
        # code here
        c = 0
        if m == 1:
            if arr[0] == 0 and n <= 1 or (arr[0] == 1 and n < 1):
                return True
            return False
        for i in range(m):
            if i == 0:
                if arr[i] == 0 and arr[i+1] == 0:
                    c += 1
                    arr[i] = 1
            else:
                if i == m - 1:
                    if arr[i-1] == 0 and arr[i] == 0:
                        c += 1
                        arr[i] = 1
                elif arr[i] == 0 and arr[i+1] != 1 and arr[i-1] != 1:
                    c += 1
                    arr[i] = 1
                else:
                    continue
                
        if c >= n:
            return True
        return False
                    



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
        
        n = int(input())
        
        
        m = int(input())
        
        
        seats=IntArray().Input(m)
        
        obj = Solution()
        res = obj.is_possible_to_get_seats(n, m, seats)
        
        result_val = "Yes" if res else "No"
        print(result_val)

# } Driver Code Ends