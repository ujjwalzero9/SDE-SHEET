# 322. Coin Change
# You are given an integer array coins representing coins of different denominations 
# and an integer amount representing a total amount of money.
# Return the fewest number of coins that you need to make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return -1.
# You may assume that you have an infinite number of each kind of coin.

# 518. Coin Change II
# You are given an integer array coins representing coins of different denominations 
# and an integer amount representing a total amount of money.
# Return the number of combinations that make up that amount. 
# If that amount of money cannot be made up by any combination of the coins, return 0.

def coinChangeFewerCoins(amount, coins):
    """
    Finds the minimum number of coins required to make up a given amount.
    
    :type amount: int
    :type coins: List[int]
    :rtype: int
    """
    # Initialize the DP array with 'infinity' for all amounts
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # Base case: 0 coins are needed to make amount 0

    # Fill the DP array using the given coins
    for coin in coins:
        for j in range(coin, amount + 1):
            dp[j] = min(dp[j], dp[j - coin] + 1)

    # Return the result or -1 if no solution exists
    return dp[amount] if dp[amount] != float("inf") else -1


def coinChangeTotalCombinations(amount, coins):
    """
    Finds the total number of combinations to make up a given amount using the given coins.
    
    :type amount: int
    :type coins: List[int]
    :rtype: int
    """
    # Initialize the DP array with 0; dp[0] = 1 (1 way to make amount 0)
    dp = [0] * (amount + 1)
    dp[0] = 1  # Base case: 1 way to make amount 0 (use no coins)

    # Fill the DP array using the given coins
    for coin in coins:
        for x in range(coin, amount + 1):
            dp[x] += dp[x - coin]

    # Return the total number of combinations
    return dp[amount]


# Driver Code
if __name__ == "__main__":
    # Test cases
    coins = [1, 2, 5]
    amount = 11

    # Testing coinChangeFewerCoins function
    print("Fewest number of coins:", coinChangeFewerCoins(amount, coins))  # Output: 3

    # Testing coinChangeTotalCombinations function
    print("Total number of combinations:", coinChangeTotalCombinations(amount, coins))  # Output: 11
