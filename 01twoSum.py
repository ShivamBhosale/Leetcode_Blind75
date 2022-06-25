# Two Sum
# Category: Array
# use hashmap to instantly check for difference value, map will add index of last occurrence of a num, don’t use same element twice

class Solution:
    def twoSum(self, nums, target):
        hashmap = {}
        for i,n in enumerate(nums):
            diff = target - nums[i]
            if diff in hashmap:
                return [hashmap[diff], i]
            hashmap[n] = i
    
print (solution.twoSum([2, 7, 11, 15], 9))
print (solution.twoSum([0, 4, 3, 0], 0))
print (solution.twoSum([-3, 4, 3, 90], 0))
        

