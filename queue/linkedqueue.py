class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next


class Queue:
    def __init__(self):
        self.linkedlist = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedlist]
        return " ".join(values)

    def enqueue(self, value):
        node = Node(value)
        if self.linkedlist.head is None:
            self.linkedlist.head = node
            self.linkedlist.tail = node
        else:
            self.linkedlist.tail.next = node
            self.linkedlist.tail = node

    def isEmpty(self):
        return True if self.linkedlist.head is None else False

    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            current = self.linkedlist.head
            if self.linkedlist.head == self.linkedlist.tail:
                self.linkedlist.head = None
                self.linkedlist.tail = None
            else:
                self.linkedlist.head = self.linkedlist.head.next
            return current

    def peek(self):
        return "Queue is empty" if self.isEmpty() else self.linkedlist.head

    def delete(self):
        self.linkedlist.head = None
        self.linkedlist.tail = None


que1 = Queue()
que1.enqueue(1)
que1.enqueue(2)
que1.enqueue(3)
print(que1)
que1.dequeue()
print(que1)




