"""

Binary Search – Search for a target in a sorted array.

"""

def binSearch(arr, ele):
    l = 0
    r = len(arr)-1
    while l <= r:
        k = (r + l) // 2
        if arr[k] == ele:
            return k
        elif arr[k] > ele:
            r = k - 1
        else:
            l = k + 1
    return -1

arr = sorted([4,7,4,6,9,3])
ele = 5
position = binSearch(arr,ele)
if position == -1: print(ele, "Not Found in", arr)
else:
    print(ele, "is", position + 1, "th position in", arr)