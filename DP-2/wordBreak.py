# 139. Word Break
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.
# Note that the same word in the dictionary may be reused multiple times in the segmentation.



class Solution(object):
    def wordBreak(self, s, wordDict):
        """
        Determines if a given string can be segmented into a space-separated 
        sequence of one or more dictionary words.

        :param s: str - The input string to segment
        :param wordDict: List[str] - List of valid dictionary words
        :return: bool - True if the string can be segmented, False otherwise
        """

        # Initialize the dp array to store the results of subproblems
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True  # Base case: An empty string can always be segmented

        # Iterate from the end of the string towards the beginning
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                # Check if the word `w` matches the substring starting at `i`
                if i + len(w) <= len(s) and s[i:i + len(w)] == w:
                    dp[i] = dp[i + len(w)]  # Update dp[i] based on the next state
                if dp[i]:  # If dp[i] is True, no need to check further words
                    break
        
        # Return whether the entire string can be segmented
        return dp[0]

# Example driver code
if __name__ == "__main__":
    solution = Solution()

    # Test Case 1
    s1 = "leetcode"
    wordDict1 = ["leet", "code"]
    print(solution.wordBreak(s1, wordDict1))  # Output: True

    # Test Case 2
    s2 = "applepenapple"
    wordDict2 = ["apple", "pen"]
    print(solution.wordBreak(s2, wordDict2))  # Output: True

    # Test Case 3
    s3 = "catsandog"
    wordDict3 = ["cats", "dog", "sand", "and", "cat"]
    print(solution.wordBreak(s3, wordDict3))  # Output: False

