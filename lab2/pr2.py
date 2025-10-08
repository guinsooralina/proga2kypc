def twoSum(nums, target):
    nums_map = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in nums_map:
            return [nums_map[complement], index]
        nums_map[num] = index

    return None  


