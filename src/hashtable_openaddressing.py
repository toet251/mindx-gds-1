class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value


class HashTable:
    def __init__(self, size=8):
        self.__size = 8
        self.__buckets = []
        for i in range(size):
            self.__buckets.append(None)

    def __hash1(self, key):
        return key % self.__size

    def __hash2(self, key):
        return 3

    def __hash(self, key, count):
        return (self.__hash1(key) + count * self.__hash2(key)) % self.__size

    def __search_pos(self, key):
        hashed = None
        count = 0
        while True:
            count += 1
            hashed = self.__hash(key, count)
            if count > self.__size or self.__buckets[hashed] == None:
                return -1
            if self.__buckets[hashed].key == key:
                return hashed
        return -1

    def insert(self, key, value):
        pos = self.__search_pos(key)

        if pos != -1:
            self.__buckets[pos] = Node(key, value)
            return

        hashed = None 
        count = 0
        while True:
            count += 1
            hashed = self.__hash(key, count)
            if count > self.__size:
                raise Exception("Hash table full to insert")
            if self.__buckets[hashed] == None or self.__buckets[hashed].key == None:
                self.__buckets[hashed] = Node(key, value)
                return

    def remove(self, key):
        pos = self.__search_pos(key)

        if pos != -1:
            self.__buckets[pos] = Node(None, None)

    def search(self, key):
        pos = self.__search_pos(key)
        if pos != -1:
            return self.__buckets[pos].value
        return None
