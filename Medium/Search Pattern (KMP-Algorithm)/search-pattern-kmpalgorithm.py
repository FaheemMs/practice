#User function Template for python3

class Solution:
    def search(self, pat, txt):
        n = len(txt)
        p = len(pat)
        i = s = 0
        res = []
        while (s < n):
            i = s
            if txt[i] == pat[0]:
                start = i
                j = 0
                while j < p and i < n and txt[i] == pat[j]:
                    i += 1
                    j += 1
                if j == p :
                    res.append(start + 1)
            s += 1
            
        return res

#initially, I wrote code without using s; I got error in a test case; I understood that iam using an 'i' pointer
#to traverse in the string, and Im incrementing the same for traversing in the pattern as well.. 
#I didnot think of "what if I never found that pattern by incrementing j (but my i is still going forward)"
#So, for traversing in the entire string -> s pointer
#if pat[0] is found, i is the one who goes on the behalf of s :)
#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        s = input().strip()
        patt = input().strip()
        ob = Solution()
        ans = ob.search(patt, s)
        if len(ans)==0:
            print(-1,end="")
        for value in ans:
            print(value,end = ' ')
        print()
# } Driver Code Ends