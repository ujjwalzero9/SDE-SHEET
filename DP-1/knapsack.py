# A thief wants to rob a store. He is carrying a bag of capacity W. 
# The store has ‘n’ items. Its weight is given by the ‘wt’ array and its value by the ‘val’ array.
#  He can either include an item in its knapsack or exclude it but can’t partially have it as a fraction.
#  We need to find the maximum value of items that the thief can steal.

def knapsack(weights, values, capacity):
    """
    This function computes the maximum value that can be obtained by the thief
    given a list of item weights, values, and the knapsack's capacity.
    """
    n = len(weights)  
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]  

    for i in range(1, n + 1):  
        for j in range(1, capacity + 1):  
            if weights[i - 1] <= j:  
                dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weights[i - 1]] + values[i - 1])
            else:
                dp[i][j] = dp[i - 1][j]  

    return dp[n][capacity]  

if __name__ == "__main__":
    weights = [2, 3, 4]  
    values = [3, 4, 5]   
    W = 5                

    max_value = knapsack(weights, values, W)
    print(f"Maximum value the thief can steal: {max_value}")
