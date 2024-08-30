#!/usr/bin/python3

def max_integer(nums=[]):
    if len(nums) == 0:
        return None

    M = nums[0]
    for i in nums:
        if i > M:
            M = i
    return M
