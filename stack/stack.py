class Stack:
    def __init__(self, maxLength):
        self.maxLength = maxLength
        self.list = []

    def __str__(self):
        return "\n".join([str(i) for i in self.list])

    def push(self, value):
        if len(self.list) == self.maxLength:
            return "Stack is already full"
        else:
            self.list.append(value)

    def pop(self):
        if len(self.list) == 0:
            return "Stack is empty"
        else:
            return self.list.pop()


    def peek(self):
        if len(self.list) == 0:
            return "Stack is empty"
        else:
            return self.list[-1]

    def isEmpty(self):
        return True if len(self.list) == 0 else False

    def isFull(self):
        return True if len(self.list) == self.maxLength else False

    def delete(self):
        self.list = None







stack1 = Stack(4)
stack1.push(10)
stack1.push(20)
stack1.push(30)
stack1.push(40)
print(stack1.isEmpty())
print(stack1.isFull())


print(stack1)
