def maxSubArray(nums):
    maxSub = nums[0]
    curSub = 0
    for i in nums:
        if curSub < 0:
            curSub = 0
        curSub += i
        maxSub = max(maxSub, curSub)``
    return maxSub

print(maxSubArray([-2,1,-3,4,-1,2,1,-5,4]))