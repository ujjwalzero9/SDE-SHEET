import sys

def matrix_chain_memoized(p):
    n = len(p) - 1  # Number of matrices
    dp = [[-1] * (n + 1) for _ in range(n + 1)]  # Memoization table
    s = [[0] * (n + 1) for _ in range(n + 1)]  # Parenthesis table
    
    def matrix_chain_recursive(i, j):
        if i == j:
            return 0
        if dp[i][j] != -1:
            return dp[i][j]
        
        min_cost = sys.maxsize
        for k in range(i, j):
            cost = (
                matrix_chain_recursive(i, k) +
                matrix_chain_recursive(k + 1, j) +
                p[i - 1] * p[k] * p[j]
            )
            if cost < min_cost:
                min_cost = cost
                s[i][j] = k
        
        dp[i][j] = min_cost
        return dp[i][j]
    
    return matrix_chain_recursive(1, n), s

def matrix_chain_gap_method(p):
    n = len(p) - 1  # Number of matrices
    dp = [[0] * (n + 1) for _ in range(n + 1)]  # DP table
    s = [[0] * (n + 1) for _ in range(n + 1)]  # Parenthesis table
    
    for length in range(2, n + 1):  # Length of subchains
        for i in range(1, n - length + 2):
            j = i + length - 1
            dp[i][j] = sys.maxsize
            for k in range(i, j):
                cost = dp[i][k] + dp[k + 1][j] + p[i - 1] * p[k] * p[j]
                if cost < dp[i][j]:
                    dp[i][j] = cost
                    s[i][j] = k
    
    return dp[1][n], s

def print_optimal_parenthesization(s, i, j):
    if i == j:
        print(f"A{i}", end="")
    else:
        print("(", end="")
        print_optimal_parenthesization(s, i, s[i][j])
        print_optimal_parenthesization(s, s[i][j] + 1, j)
        print(")", end="")

# Example usage:
p = [30, 35, 15, 5, 10, 20, 25]  # Matrix dimensions

# Using Memoized Recursion
min_cost_memo, s_memo = matrix_chain_memoized(p)
print("Using Memoization:")
print("Minimum number of multiplications:", min_cost_memo)
print("Optimal Parenthesization:", end=" ")
print_optimal_parenthesization(s_memo, 1, len(p) - 1)
print("\n")

# Using Gap Method (Bottom-Up DP)
min_cost_gap, s_gap = matrix_chain_gap_method(p)
print("Using Gap Method:")
print("Minimum number of multiplications:", min_cost_gap)
print("Optimal Parenthesization:", end=" ")
print_optimal_parenthesization(s_gap, 1, len(p) - 1)
print()
