 # 416. Partition Equal Subset Sum
# -------------------------------
# Given an integer array nums, return true if you can partition the array into 
# two subsets such that the sum of the elements in both subsets is equal, or 
# false otherwise.

# Example 1:
# Input: nums = [1, 5, 11, 5]
# Output: true
# Explanation: The array can be partitioned as [1, 5, 5] and [11].

# Example 2:
# Input: nums = [1, 2, 3, 5]
# Output: false
# Explanation: The array cannot be partitioned into equal subsets.

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total_sum = sum(nums)
        
        # If total sum is odd, partition is not possible
        if total_sum % 2 != 0:
            return False
        
        # Target sum for each partition
        target = total_sum // 2
        
        # Initialize dp array where dp[i] means whether a subset with sum i is possible
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: sum 0 is always achievable
        
        for num in nums:
            # Traverse backwards to avoid recomputation using the same num
            for j in range(target, num - 1, -1):
                dp[j] = dp[j] or dp[j - num]
        
        # Return whether it's possible to get a subset with sum equal to target
        return dp[target]

# Driver code
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        [1, 5, 11, 5],       # Expected: True
        [1, 2, 3, 5],        # Expected: False
        [1, 2, 3, 4, 5],     # Expected: True
        [2, 2, 3, 5]         # Expected: True
    ]

    for nums in test_cases:
        result = solution.canPartition(nums)
        print(f"Input: {nums} -> Can partition: {result}")
