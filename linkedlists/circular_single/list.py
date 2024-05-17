
class Node:
    def __init__(self, value = 0, next = None):
        self.value = value
        self.next = next

    def __str__(self) -> str:
        return str(self.value)

class CircularList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        result = ''
        temp_node = self.head
        while temp_node is not None:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:
                break
            result += ' -> '
        return result

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.length = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node
        self.length += 1


    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            raise Exception("Index out of range")
        if index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                self.tail.next = new_node
                new_node.next = self.head
                self.head = new_node
        elif index == self.length:
            self.tail.next = new_node
            self.tail = new_node
            new_node.next = self.head
        else:
            temp_node = self.head
            for _ in range(index-1):
                temp_node = temp_node.next
            new_node.next = temp_node.next
            temp_node.next = new_node
        self.length += 1

    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            if current.next == self.head:
                break
            else:
                current = current.next

    def search(self, value):
        current = self.head
        while current is not None:
            if current.value == value:
                return True
            if current.next == self.head:
                break
            current = current.next
        return False

    def get_value(self, index):
        if index == -1:
            return self.tail
        elif index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def set_value(self, index, value):
        if index == -1:
            self.tail.value = value
        elif index < 0 or index >= self.length:
            return None
        current = self.head
        for _ in range(index):
            current = current.next
        current.value = value

    def set_value_other_way(self, index, value):
        temp = self.get_value(index)
        if temp:
            temp.value = value
            return True
        return False

    def pop_first(self):
        popped_node = self.head
        if self.length == 0:
            return None
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node

    def pop(self):
        popped_node = self.tail
        if self.length == 0:
            return None
        elif self.length == 1:
            self.head = None
            self.length = None
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            temp.next = self.head
            self.tail = temp
            popped_node.next = None
        self.length -= 1
        return popped_node

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None
        elif index == 0:
            return self.pop_first()
        elif index == self.length -1:
            return self.pop()
        prev_node = self.get_value(index-1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node

    def delete_items(self):
        if self.length == 0:
            return
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0
    





llist1 = CircularList()
llist1.append(10)
llist1.append(20)
#print(llist1)
llist1.prepend(30)
#print(llist1)
llist1.insert(2,40)
#print(llist1)
llist1.insert(4,50)
#print(llist1)
llist1.insert(0,60)
print(llist1)
llist1.traverse()
print(llist1.search(50))
print(llist1.search(90))
print(llist1.get_value(2))
print(llist1.set_value(2,99))
print(llist1)
llist1.set_value_other_way(3,888)
print(llist1)
print(llist1.pop_first())
print(llist1)
print(llist1.pop())
print(llist1)
print(llist1.remove(2))
print(llist1)

