"""

Top-K Frequent Elements - Return the k most frequent numbers in an array.

"""    

def freqNums(arr, k):
    freq = {}
    for a in arr:
        if a in freq: freq[a] += 1  
        else: freq[a] = 1
    dic = dict(sorted(freq.items(), key=lambda item: item[1]))
    keys = list(reversed(list(dic.keys())))
    out = list(keys[:k])
    return out


print(freqNums([1,1,1,1,2,3,4,2,3,4,4,4,4,4,4,4,3,2, 5,5,5,5,5,5,5,5,5,5,5], 2))