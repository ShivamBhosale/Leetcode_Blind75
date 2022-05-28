def containsDuplicate(nums):
    if len(set(nums)) == len(nums):
        return False
    else:
        return True
    
print(containsDuplicate([1,2,3,4,4,5]))