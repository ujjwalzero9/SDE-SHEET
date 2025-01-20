# Function to calculate the maximum sum of a strictly increasing subsequence in an array.
# Given an array of positive integers, the function finds the subsequence where the integers are sorted in strictly increasing order 
# and the sum of the elements in that subsequence is maximized.

def maxSumIncreasingSequence(nums):
    """
    Calculate the maximum sum of a strictly increasing subsequence in the given list of integers.

    Parameters:
    nums (list): A list of positive integers representing the array.

    Returns:
    int: The maximum sum of an increasing subsequence in the array.
    
    This function uses dynamic programming. It iterates through the list and updates the dp array,
    where dp[i] stores the maximum sum of the increasing subsequence ending at index i.
    """
    n = len(nums)
    dp = nums[:]
    
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + nums[i]:
                dp[i] = dp[j] + nums[i]
    
    return max(dp)


def printmaxSumIncreasingSequence(nums):
    """
    Calculate and print the maximum sum of a strictly increasing subsequence and the subsequence itself.

    Parameters:
    nums (list): A list of positive integers representing the array.

    Returns:
    tuple: A tuple containing:
        - The maximum sum of the increasing subsequence (int).
        - The longest increasing subsequence (list).
    
    This function uses dynamic programming and backtracking to both calculate the maximum sum of an increasing subsequence 
    and reconstruct the subsequence by using a parent array.
    """
    n = len(nums)
    dp = nums[:]
    parent = [-1] * n
    
    for i in range(n):
        for j in range(i):
            if nums[i] > nums[j] and dp[i] < dp[j] + nums[i]:
                dp[i] = dp[j] + nums[i]
                parent[i] = j
    
    max_sum = max(dp)
    max_ind = dp.index(max_sum)
    
    lis = []
    current = max_ind
    while current != -1:
        lis.append(nums[current])
        current = parent[current]
    
    lis.reverse()
    
    return max_sum, lis


if __name__ == "__main__":
   
    nums = [3, 4, 5, 10, 7, 8, 20]

    

    # Test maxSumIncreasingSequence function
    max_sum = maxSumIncreasingSequence(nums)
    print(f"Maximum sum of increasing subsequence: {max_sum}")

    print("------------------------------------------")
    max_sum, lis = printmaxSumIncreasingSequence(nums)
    print(f"Maximum sum of increasing subsequence: {max_sum}")
    print(f"Longest increasing subsequence: {lis}")