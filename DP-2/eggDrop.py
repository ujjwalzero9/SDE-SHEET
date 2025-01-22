# Egg Dropping Puzzle : https://www.geeksforgeeks.org/problems/egg-dropping-puzzle-1587115620/1
#You are given n identical eggs and you have access to a k-floored building from 1 to k.

# There exists a floor f where 0 <= f <= k such that any egg dropped from a floor higher than f will break, and any egg dropped from or below floor f will not break.
# There are few rules given below. 

# An egg that survives a fall can be used again.
# A broken egg must be discarded.
# The effect of a fall is the same for all eggs.
# If the egg doesn't break at a certain floor, it will not break at any floor below.
# If the egg breaks on a certain floor, it will break on any floor above.
# Return the minimum number of moves you need to determine the value of f with certainty.


class Solution:
    """
    A class to solve the Egg Drop problem using recursion with memoization.
    """

    def eggDrop(self, n, k):
        """
        Function to find the minimum number of attempts needed in the worst case 
        to find the critical floor using n eggs and k floors.

        :param n: int - Number of eggs
        :param k: int - Number of floors
        :return: int - Minimum number of attempts required in the worst case
        """
        # Memoization table, initialized to -1
        dp = [[-1] * (k + 1) for _ in range(n + 1)]

        def solve(n, k):
            """
            A helper function to calculate the minimum attempts for n eggs and k floors.
            
            :param n: int - Number of eggs
            :param k: int - Number of floors
            :return: int - Minimum attempts for the given parameters
            """
            # Base cases
            if k == 0:  # No floors
                return 0
            if n == 1:  # Only one egg
                return k
            if k == 1:  # Only one floor
                return 1

            # Return cached result if already computed
            if dp[n][k] != -1:
                return dp[n][k]

            mn = float('inf')  # Initialize the minimum attempts to infinity

            # Try dropping the egg from each floor (1 to k)
            for i in range(1, k + 1):
                # Two cases:
                # 1. Egg breaks: Check floors below (n-1 eggs, i-1 floors)
                # 2. Egg does not break: Check floors above (n eggs, k-i floors)
                tmp = max(solve(n - 1, i - 1), solve(n, k - i)) + 1
                
                # Update the minimum attempts
                mn = min(mn, tmp)

            dp[n][k] = mn  # Memoize the result
            return dp[n][k]

        # Start recursion with n eggs and k floors
        return solve(n, k)


# Driver Code
def main():
    """
    Main function to test the eggDrop function.
    """
    # Create an instance of the Solution class
    solution = Solution()

    # Example 1
    n1, k1 = 2, 10
    print(f"Minimum attempts needed with {n1} eggs and {k1} floors:", solution.eggDrop(n1, k1))

    # Example 2
    n2, k2 = 3, 5
    print(f"Minimum attempts needed with {n2} eggs and {k2} floors:", solution.eggDrop(n2, k2))

    # Example 3
    n3, k3 = 1, 6
    print(f"Minimum attempts needed with {n3} eggs and {k3} floors:", solution.eggDrop(n3, k3))


if __name__ == "__main__":
    main()








