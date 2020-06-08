
class Node:
    def __init__(self, value=None, next=None):
        self.value = value 
        self.next = next 


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.__size = self.__count_size() 

    def __count_size(self):
        count = 0
        node = self.head 
        while node:
            count += 1
            node = node.next
        return count
    
    def size(self):
        return self.__size
        
    def is_empty(self):
        return self.__size == 0

    def value_at(self, index):
        if index < 0 or index >= self.__size:
            raise Exception("Index out of range")
        i = 0 
        node = self.head 
        while i < index:
            node = node.next
            i += 1
        return node.value
    
    def push_front(self, value):
        node = Node(value, self.head)
        self.head = node
        self.__size += 1
    
    def pop_front(self):
        if self.is_empty():
            raise Exception("Can not pop front of the empty linked list")
        value = self.head.value 
        self.head = self.head.next 
        self.__size -= 1
        return value 

    def push_back(self, value):
        new_node = Node(value)
        if self.is_empty():
            self.head = new_node
            self.__size += 1
            return

        node = self.head 
        while node.next:
            node = node.next 
        node.next = new_node
        self.__size += 1

    def pop_back(self):
        if self.is_empty():
            raise Exception("Can not pop back of the empty linked list")
        
        node = self.head
        pre = None 
        while node.next:
            pre = node 
            node = node.next
        
        value = node.value 
        if pre:
            pre.next = None 
        else:
            self.head = None 
        self.__size -= 1
        return value 

    def front(self):
        if self.is_empty():
            raise Exception("Can not get front of empty linked list")
        return self.head.value
    
    def back(self):
        if self.is_empty():
            raise Exception("Can not get back of empty linked list")
        node = self.head
        while node.next:
            node = node.next 
        return node.value

    def insert(self, value, index):
        if index < 0 or index > self.__size:
            raise Exception("Invalid index to insert")
        if index == 0:
            self.push_front(value)
            return 
    
        i = 0
        node = self.head
        pre = None 
        while i < index:
            pre = node 
            node = node.next
            i += 1

        new_node = Node(value)
        new_node.next = node
        pre.next = new_node
        self.__size += 1

    def remove_at(self, index):
        if index < 0 or index >= self.__size:
            raise Exception("Invalid index to insert")
        if index == 0:
            self.pop_front()
            return 

        i = 0
        node = self.head 
        while i < index-1:
            node = node.next
            i += 1
        node.next = node.next.next

    def display(self):
        arr = []
        node = self.head
        while node:
            arr.append(node.value)
            node = node.next
        print(f"Cap: {self.__size} Values: {arr}")
