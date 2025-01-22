# 131. Palindrome Partitioning
# Given a string s, partition s such that every substringof the partition is a palindrome
# Return all possible palindrome partitioning of s.

class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """

        res = []  # List to store all valid palindrome partitions
        part = []  # Temporary list to store the current partition

        def dfs(i):
            """
            Perform depth-first search to find all palindrome partitions.
            :param i: Current starting index for partitioning
            """
            if i >= len(s):  # Base case: If we reach the end of the string
                res.append(part.copy())  # Add a copy of the current partition to the result
                return
            for j in range(i, len(s)):  # Iterate over possible partition end indices
                if self.isPalindrome(s, i, j):  # Check if the substring is a palindrome
                    part.append(s[i:j + 1])  # Add the palindrome substring to the current partition
                    dfs(j + 1)  # Recur for the remaining substring
                    part.pop()  # Backtrack by removing the last added palindrome substring

        dfs(0)  # Start DFS from the beginning of the string
        return res

    def isPalindrome(self, s, i, j):
        """
        Check if a substring is a palindrome.
        :param s: str - The input string
        :param i: int - Starting index of the substring
        :param j: int - Ending index of the substring
        :return: bool - True if the substring is a palindrome, False otherwise
        """
        while i < j:
            if s[i] != s[j]:  # Characters at i and j don't match
                return False
            i += 1  # Move the start pointer forward
            j -= 1  # Move the end pointer backward
        return True
    



    



if __name__ == "__main__":
    solution = Solution()

    # Test case 1
    s1 = "aab"
    print(solution.partition(s1))  # Output: [["a", "a", "b"], ["aa", "b"]]

    # Test case 2
    s2 = "racecar"
    print(solution.partition(s2))  
    # Output: [["r", "a", "c", "e", "c", "a", "r"], ["r", "a", "cec", "a", "r"], ["racecar"]]

    # Test case 3
    s3 = "a"
    print(solution.partition(s3))  # Output: [["a"]]
