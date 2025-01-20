#Revision Needed
def matrixChainMultiplication(nums):
    n = len(nums) - 1
    dp = [[0] * n for _ in range(n)]

    for length in range (2, n+1):
        for i in range(n + 1 - length):
            j = i + length - 1  
            dp[i][j] = float('inf') 
            for k in range(i, j): 
                q = dp[i][k] + dp[k + 1][j] + nums[i] * nums[k + 1] * nums[j + 1]
                if q < dp[i][j]:
                    dp[i][j] = q  
    
        return dp[0][n - 1]

