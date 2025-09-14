"""

Rotate Array : 
Rotate an array to the right by k steps.

"""

def rotate1(arr, k): # Using Slicing
    k %= len(arr)
    first_n_k_elements = arr[:len(arr)-k]
    last_k_elements = arr[len(arr)-k:]
    return last_k_elements + first_n_k_elements

def rotate2(arr,k): # Without Slicing
    k %= len(arr)
    def reverse(start, end):
        arr[start : end+1] = reversed(arr[start : end+1])
    reverse(0, len(arr)-k-1)
    reverse(len(arr)-k, len(arr)-1)
    reverse(0, len(arr)-1)
    return arr

a = [1,2,3,4,5,6,7,8,9]
print(rotate1(a, 4))
print(rotate2(a, 4))