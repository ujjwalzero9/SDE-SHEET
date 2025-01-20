# 1143. Longest Common Subsequence
# PS: Given two strings `str1` and `str2`, return the length of their longest common subsequence.
# A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.
# For example, given the strings "abcde" and "ace", the longest common subsequence is "ace", and its length is 3.

def LongestCommonSubsequence(str1, str2):
    """
    Function to compute the length of the Longest Common Subsequence (LCS) 
    between two strings using dynamic programming.

    Parameters:
    str1 (str): The first input string.
    str2 (str): The second input string.

    Returns:
    int: The length of the Longest Common Subsequence.
    
    The function uses a 2D DP table to store the lengths of LCS for different
    substrings of str1 and str2, and computes the final LCS length iteratively.
    """
    n = len(str1)
    m = len(str2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp[n][m]

def LongestCommonSubsequence(str1, str2):
    """
    Function to compute the Longest Common Subsequence (LCS) between two 
    strings and return the actual LCS sequence.

    Parameters:
    str1 (str): The first input string.
    str2 (str): The second input string.

    Returns:
    str: The Longest Common Subsequence as a string.
    
    The function uses a 2D DP table to compute the length of LCS and 
    traces back through the table to reconstruct the actual LCS sequence.
    """
    n = len(str1)
    m = len(str2)

    dp = [[0] * (m + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    i, j = n, m
    lcs = []
    while i > 0 and j > 0:
        if str1[i - 1] == str2[j - 1]:
            lcs.append(str1[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    lcs = "".join(reversed(lcs))

    print(lcs)
    return dp[n][m]


if __name__ == "__main__":
    a = LongestCommonSubsequence("abcde", "ace")
    print(a)
