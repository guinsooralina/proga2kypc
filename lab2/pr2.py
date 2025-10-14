def two_sum(nums, target):
    num_x = {}
    for index, num in enumerate(nums):
        complement = target - num
        if complement in num_x:
            return [num_x[complement], index]
        num_x[num] = index
    print("нет подходящих слагаемых для заданной суммы.")
    return None

