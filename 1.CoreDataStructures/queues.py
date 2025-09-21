"""

Queue Using Stacks : Implement a queue using two stacks

"""

class Queue:
    def __init__(self):
        self.content = []
    def enqueue (self, x):
        self.content.append(x)
    def dequeue(self):
        if not self.content: return None
        return self.content.pop(0)
    def display(self):
        print(self.content)

q = Queue()
q.enqueue(4)
q.enqueue(2)
q.enqueue(5)
q.enqueue(1)
q.enqueue(3)
q.display() # [4, 2, 5, 1, 3]
q.dequeue()
q.dequeue()
q.dequeue()
q.display() # [1, 3]
    