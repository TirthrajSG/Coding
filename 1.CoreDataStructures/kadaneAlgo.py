"""

Maximum Subarray (Kadane's Algorithm) :
Find the contiguous subarray with the largest sum.

"""

def kadaneAlgo(arr):
    max_sum = float('-inf')
    current_sum = float("-inf")
    for i in arr:
        current_sum = max(i, current_sum + i)
        max_sum = max(max_sum, current_sum)

    return max_sum

a = [-5,-4,-5,-3,-5,-3,-5,-7,-2,-1,-3,-5]
print(kadaneAlgo(a))