#User function Template for python3
class Solution:
    
    # Note that the size of the array is n-1
    def missingNumber(self, n, arr):
        # code here
        s1 = set(arr)
        s2 = set()

        for i in range(1,n+1):
            s2.add(i)
        
        s = s2.difference(s1)
        
        for i in s:
            return i
         

#{ 
 # Driver Code Starts
#Initial Template for Python 3

t = int(input())
for _ in range(0, t):
    n = int(input())
    arr = list(map(int, input().split()))
    s = Solution().missingNumber(n, arr)
    print(s)

# } Driver Code Ends
