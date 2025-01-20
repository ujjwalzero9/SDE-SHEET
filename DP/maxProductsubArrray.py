# Leetcode 152: Maximum Product Subarray
# Problem Statement:
# Given an integer array nums, find the contiguous subarray within an array (containing at least one number) 
# which has the largest product, and return its product.

def maxProduct_simple(nums):
    """
    Calculates the maximum product of any contiguous subarray by considering prefix and suffix products.
    It iterates through the array to track the highest product possible without returning the subarray.
    """
    n = len(nums)
    pre, suff = 1, 1
    ans = float('-inf')

    for i in range(n):
        if pre == 0:
            pre = 1
        if suff == 0:
            suff = 1
        
        pre *= nums[i]
        suff *= nums[n - i - 1]
        
        ans = max(ans, max(pre, suff))

    return ans

def maxProduct(nums):
    """
    Finds the maximum product of any contiguous subarray and returns the subarray that produces this maximum product.
    It uses prefix and suffix products to track the maximum product and its corresponding subarray.
    """
    n = len(nums)
    
    if n == 0:
        return 0, nums
    
    prefix = suffix = 1
    pre_start = pre_end = 0
    suff_start = suff_end = n - 1
    best_start = best_end = 0
    maxProduct = float("-inf")
    
    for i in range(n):
        prefix *= nums[i]
        suffix *= nums[n - 1 - i]

        if maxProduct < max(prefix, suffix):
            maxProduct = max(prefix, suffix)
            if prefix > suffix:
                best_start = pre_start
                best_end = i
            else:
                best_start = i
                best_end = suff_end

        if prefix == 0:
            prefix = 1
            pre_start = i
        if suffix == 0:
            suffix = 1
            suff_end = i
    
    subarray = nums[best_start:best_end + 1]
    
    return maxProduct, subarray

# Driver code
if __name__ == "__main__":
    arr = [2, 3, -2, 4]
    
    max_prod_simple = maxProduct_simple(arr)
    print(f"Maximum Product (Simple): {max_prod_simple}")
    
    max_prod, subarray = maxProduct(arr)
    print(f"Maximum Product: {max_prod}")
    print(f"Subarray: {subarray}")
