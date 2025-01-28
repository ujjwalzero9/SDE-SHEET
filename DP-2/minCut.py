# Given a string s, a partitioning of the string is a palindrome partitioning if every sub-string of the partition is a palindrome.
# Determine the fewest cuts needed for palindrome partitioning of the given string.
class Solution:
    def minCut(self, s: str) -> int:
        # dp[i] will store the minimum number of cuts needed for substring s[0:i+1]
        dp = [i for i in range(len(s))]

        # A helper function to check if a substring s[i:j+1] is a palindrome
        def isPalindrome(i, j):
            while i < j:
                if s[i] != s[j]:
                    return False
                i += 1
                j -= 1
            return True

        # Iterate over the string
        for i in range(1, len(s)):
            # Check all possible partitions
            for j in range(i + 1):
                if isPalindrome(j, i):
                    dp[i] = min(dp[i], dp[j - 1] + 1 if j > 0 else 0)

        return dp[-1]


# Driver code
if __name__ == "__main__":
    solution = Solution()

    # Test cases
    test_cases = [
        "aab",         # Expected output: 1 (cut between 'a' and 'ab')
        "a",           # Expected output: 0 (already a palindrome)
        "abac",         # Expected output: 1 (cut between 'ab' and 'ac')
        "abcba",        # Expected output: 0 (already a palindrome)
        "ab"            # Expected output: 1 (cut between 'a' and 'b')
    ]

    for test in test_cases:
        print(f"Minimum cuts for '{test}': {solution.minCut(test)}")
