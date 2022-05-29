# Maximum Product Subarray
def maxProduct(nums):
    res = max(nums)
    curMax, curMin = 1,1
    
    for n in nums:
        if n == 0:
            curMax, curMin = 1,1
            continue
        temp = curMax * n
        curMax = max(n*curMax,n*curMin,n)
        curMin = min(temp,n*curMin,n)
        res = max(res,curMax)
    return res

print(maxProduct([2,3,-2,4]))



