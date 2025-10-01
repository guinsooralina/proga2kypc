def twoSum(nums, target):
    nums_map = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in nums_map:
            return [nums_map[complement], index]
        nums_map[num] = index

    return None  

nums1 = [2, 7, 11, 15]
target1 = 9
print(twoSum(nums1, target1)) 

nums2 = [3, 2, 4]
target2 = 6
print(twoSum(nums2, target2))  

nums3 = [3, 3]
target3 = 6
print(twoSum(nums3, target3)) 
