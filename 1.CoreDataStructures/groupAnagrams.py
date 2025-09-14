"""

Group Anagrams : Group words that are anagrams of each other.

"""

def group1(arr): # Intuitive
    def isAnagram(x,y):
        return sorted(x) == sorted(y)
    out = []
    while arr:
        i = 0
        temp = []
        temp.append(arr.pop(0))
        while i < len(arr):
            if isAnagram(arr[i],temp[0]): 
                temp.append(arr[i])
                arr.pop(i)
            else: i += 1
        out.append(temp)
    return out

def group2(arr): # Hashmaps
    groups = {}
    for word in arr:
        key = "".join(sorted(word))
        if key not in groups: groups[key] = []
        groups[key].append(word)
    return list(groups.values()) 


a = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group1(a))
a = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group2(a))
