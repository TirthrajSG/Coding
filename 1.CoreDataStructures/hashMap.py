"""

Design Hashmap : Implement a basic hashmap without using built-in dicts.

"""

class HashMap:
    def __init__(self):
        self.keys = []
        self.values = []
    def put(self, key, value):
        if key in self.keys:
            index = self.keys.index(key)
            self.values[index] = value
        else:
            self.keys.append(key)
            self.values.append(value)
    def get(self, key):
        try:
            index = self.keys.index(key)
            return self.values[index]
        except: return None
    def remove(self, key):
        try:
            index = self.keys.index(key)
            self.keys.pop(index)
            self.values.pop(index)
        except: print(f"{key} not in Keys")
    def __str__(self):
        return str(list(zip(self.keys, self.values)))


hmap = HashMap()

hmap.put("apple", 10)
hmap.put("banana", 20)
hmap.put("orange", 30)
print(hmap.get("apple"))    # 10
print(hmap.get("banana"))   # 20

hmap.put("apple", 50)       # update
print(hmap.get("apple"))    # 50

hmap.remove("banana")
print(hmap.get("banana"))   # None

print(hmap)   # [('apple', 50), ('orange', 30)]  