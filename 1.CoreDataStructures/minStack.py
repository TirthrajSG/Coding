"""

Min Stack : Implement a stack that supports push, pop, and retrieving the minimum in O(1).

"""

class Stack:
    def __init__(self):
        self.content = []
        self.minimum = []
    def push(self, s):
        self.content.append(s)
        if not self.minimum or s <= self.minimum[-1]:
            self.minimum.append(s)
    def pop(self):
        if not self.content:
            return None
        val = self.content.pop()
        if val == self.minimum[-1]:
            self.minimum.pop()
        return val
    def min(self):
        if not self.minimum: return None
        return self.minimum[-1]
    def print(self):
        print(self.content)

s1 = Stack()
s1.push(4)
s1.push(3)
s1.push(2)
s1.push(1)
s1.push(5)
s1.push(3)
s1.print() # [4, 3, 2, 1, 5, 3]
s1.pop()
s1.pop()
s1.pop()
s1.print() # [4, 3, 2]
print(s1.min()) # 2