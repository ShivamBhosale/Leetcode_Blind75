# With the division operator
# def productExceptSelf(nums):
#     prod_array=[]
#     prod = 1
#     for i in range(len(nums)):
#         prod = prod * nums[i]
#     for i in range(len(nums)):
#         final = prod // nums[i]
#         prod_array.append(final)
#     return prod_array   
       
# print(productExceptSelf([1,2,3,4]))
    
# But the question demands to solve the problem in O(n) and without the division operator

def productExceptSelf2(nums):
    prod_array = [1] * len(nums)
    #prefix
    prefix = 1
    for i in range(len(nums)):
        prod_array[i] = prefix
        prefix *= nums[i]
    #postfix
    postfix = 1
    for i in range(len(nums)-1,-1,-1):
        prod_array[i] *= postfix
        postfix *= nums[i]
    return prod_array
print(productExceptSelf2([1,2,3,4]))


