class Queue:
    def __init__(self, cap):
        self.__cap = cap
        self.__vals = [None] * cap 
        self.__in = 0
        self.__out = 0
        self.__size = 0

    def enqueue(self, val):
        if self.__is_full():
            raise Exception('Queue full')
        self.__vals[self.__in] = val 
        self.__in = (self.__in + 1) % self.__cap
        self.__size += 1

    def dequeue(self):
        if self.__is_empty():
            raise Exception('Queue empty')
        val = self.__vals[self.__out]
        self.__vals[self.__out] = None
        self.__out = (self.__out + 1) % self.__cap
        self.__size -= 1
        return val 

    def front(self):
        if self.__is_empty():
            raise Exception('Queue empty')
        val = self.__vals[self.__out]
        return val 

    def __is_empty(self):
        return self.__size == 0

    def __is_full(self):
        return self.__size == self.__cap 

