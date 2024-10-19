def twoSum(nums, target):
    listLen = len(nums)

    for i in range(listLen-1):
        for j in range(i+1, listLen):
            if (nums[i] + nums[j] == target):
                return [i, j]
            
    return 0

# test cases
print(twoSum([2, 7, 11, 15], 9))
print(twoSum([3, 2, 4], 6))
print(twoSum([3, 3], 6))