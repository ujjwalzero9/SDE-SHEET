# Leetcode 300. Longest Increasing Subsequence

# Problem Statement:
# Given an integer array nums, return the length of the longest strictly increasing subsequence.

def LIS(nums):
    """
    Function to calculate the length of the longest increasing subsequence (LIS) in a given list of integers.
    
    Parameters:
    nums (list): A list of integers to find the LIS in.

    Returns:
    int: The length of the longest strictly increasing subsequence in the list.
    
    The function uses dynamic programming to calculate the LIS length.
    """
    n = len(nums)
    dp = [1] * n
    
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] + 1)
    
    print(dp)
    return dp[n-1]


def printLIS(nums):
    """
    Function to find and print the longest increasing subsequence (LIS) in a given list of integers.
    
    Parameters:
    nums (list): A list of integers to find the LIS in.
    
    Returns:
    tuple: A tuple containing:
        - The length of the longest increasing subsequence (int).
        - The longest increasing subsequence itself (list).
        
    The function uses dynamic programming and backtracking to reconstruct the LIS.
    """
    n = len(nums)
    dp = [1] * n
    parent = [-1] * n
    
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + 1:
                dp[i] = dp[j] + 1
                parent[i] = j
    
    subArray = []
    current = dp.index(max(dp))
    while current != -1:
        subArray.append(nums[current])
        current = parent[current]
    
    subArray.reverse()
    
    print(subArray)
    print(dp)
    
    return max(dp), subArray
