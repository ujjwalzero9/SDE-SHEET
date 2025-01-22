# 1547. Minimum Cost to Cut a Stick
# Given a wooden stick of length n units. 
# The stick is labelled from 0 to n. For example, a stick of length 6 is labelled as follows:
# Given an integer array cuts where cuts[i] denotes a position you should perform a cut at.
#You should perform the cuts in order, you can change the order of the cuts as you wish.

class Solution(object):
    def minCostRodCutting(self, n, cuts):
        """
        Calculate the minimum cost to cut a stick.
        
        :param n: int - The total length of the stick.
        :param cuts: List[int] - Positions where the stick needs to be cut.
        :return: int - The minimum cost of performing all cuts.
        """
        dp = {}  # Dictionary for memoization
        
        def dfs(l, r):
            """
            A recursive function to calculate the minimum cost of cutting a stick 
            between points cuts[l] and cuts[r].
            
            :param l: int - Index of the left boundary in the cuts array.
            :param r: int - Index of the right boundary in the cuts array.
            :return: int - Minimum cost for cutting the stick in the range.
            """
            if r - l == 1:  # Base case: No segment between l and r
                return 0
            if (l, r) in dp:  # Return cached result if exists
                return dp[(l, r)]
            
            res = float('inf')  # Initialize result to infinity
            
            # Iterate through possible cuts within the current range
            for cut  in cuts:
                if l < cut < r:
                    res = min(res, dfs(l, cut) + dfs(cut, r) + (r - l))
            
            dp[(l, r)] = res = 0 if res == float('inf') else res
            return res
        
        # Start recursion between the first and last positions
        return dfs(0, n)


# Driver Code
if __name__ == "__main__":
    # Example 1
    n = 7
    cuts = [1, 3, 4, 5]
    solution = Solution()
    print("Minimum cost to cut the stick:", solution.minCostRodCutting(n, cuts))
    
    # Example 2
    n = 9
    cuts = [5, 6, 1, 4, 2]
    print("Minimum cost to cut the stick:", solution.minCostRodCutting(n, cuts))
