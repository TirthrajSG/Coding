""" 
Two Sum:
Given an array and a target, return indices of two numbers 
that add up to the target.

"""

def twoSum(arr,target):
    seen = {}
    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return seen[complement], i
        seen[num] = i
    return -1


a = [5,4,4,6,9,2,8]
target = 8

print(twoSum(a,target))