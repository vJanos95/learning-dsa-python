class Queue:
    def __init__(self, maxLength):
        self.list = []
        self.maxLength = maxLength

    def __str__(self):
        values = [str(x) for x in self.list]
        return "\n".join(values)

    def isFull(self):
        return True if len(self.list) == self.maxLength else False

    def isEmpty(self):
        return True if len(self.list) == 0 else False

    def enqueue(self, value):
        if self.isFull():
            return "Queue is full"
        else:
            self.list.append(value)

    def dequeue(self):
        if self.isEmpty():
            return "Queue is already empty"
        else:
            self.list.pop(0)
    
    def peek(self):
        return self.list[0]

    def delete(self):
        self.list = None

que1 = Queue(5)
que1.enqueue(1)
que1.enqueue(2)
que1.enqueue(3)
que1.enqueue(4)
print(que1)
print(que1.isEmpty())
que1.enqueue(5)
print(que1.isFull())
que1.dequeue()
print(que1.peek())
print("///")
print(que1)






