class Node:
    def __init__(self, key=None, value=None, next=None):
        self.key = key
        self.value = value 
        self.next = next


class HashTable:
    def __init__(self, size=8):
        self.__size = size
        self.__buckets = []
        for i in range(size):
            self.__buckets.append(Node(None, None, None))

    def __hash(self, key):
        return hash(key) % self.__size

    def insert(self, key, value):
        hash_key = self.__hash(key)

        node = self.__buckets[hash_key]
        pre = None
        while node:
            if node.key == key:
                node.value = value 
                return
            pre = node
            node = node.next

        pre.next = Node(key, value, None)

    def get(self, key):
        hash_key = self.__hash(key)

        node = self.__buckets[hash_key]
        while node:
            if node.key == key:
                return node.value 
            node = node.next 
        return None

    def remove(self, key):
        hash_key = self.__hash(key)

        node = self.__buckets[hash_key]
        pre = None
        while node:
            if node.key == key:
                pre.next = node.next
                return
            pre = node
            node = node.next
    