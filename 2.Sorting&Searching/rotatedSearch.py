"""

Search in Rotated Sorted Array : Find an element in a rotated sorted array.

"""

def rotatedSearch(arr, ele):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = left + (right - left)//2
        if ele == arr[mid]: return mid

        if arr[left] <= arr[mid]: # If left subarray is sorted
            if arr[left] <= ele < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else: # If Right subarray is sorted
            if arr[mid] < ele <= arr[right]:
                left = mid + 1
            else:
                right = mid - 1
    return -1

arr = [4,5,6,7,0,1,2]
ele = 0
print(rotatedSearch(arr,ele))