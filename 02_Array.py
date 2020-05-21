class Array:
    def __init__(self, capacity):
        self.__arr = [None] * capacity
        self.__size = 0
        self.__capacity = capacity

    def __expand(self):
        """ Expand array to double capacity
        """
        new_capacity = self.__capacity * 2 + 1
        self.__clone_to_capacity(new_capacity)

    def __shrink(self):
        """ Shrink array to half capacity
        """
        new_capacity = int(self.__capacity / 2)
        self.__clone_to_capacity(new_capacity)
    
    def __clone_to_capacity(self, new_capacity):
        new_arr = [None] * new_capacity
        for i in range(self.__size):
            new_arr[i] = self.__arr[i]
        self.__capacity = new_capacity
        self.__arr = new_arr

    def size(self):
        return self.__size

    def capacity(self):
        return self.__capacity

    def is_empty(self):
        return self.__size == 0

    def __is_full(self):
        return self.__size == self.__capacity

    def item_at(self, index):
        if index < 0 or index >= self.__size:
            raise Exception("Invalid index to get item")
        return self.__arr[index]

    def append(self, value):
        if self.__is_full():
            self.__expand()
        self.__arr[self.__size] = value
        self.__size += 1

    def insert(self, value, index):
        if index < 0 or index > self.__size:
            raise Exception("Invalid index to insert")
        if self.__is_full():
            self.__expand()
        i = self.__size
        while i > index:
            self.__arr[i] = self.__arr[i-1]
            i -= 1
        self.__arr[index] = value
        self.__size += 1
    
    def pop(self):
        if self.is_empty():
            raise Exception("Empty array to pop")
        pop_value = self.__arr[self.__size-1]
        self.__arr[self.__size-1] = None
        self.__size -= 1

        if self.__size <= self.__capacity / 4:
            self.__shrink()
        return pop_value
    
    def remove_at(self, index):
        if index < 0 or index >= self.__size:
            raise Exception("Invalid index to remove")
        i = index
        while i < self.__size - 1:
            self.__arr[i] = self.__arr[i+1]
            i += 1
        self.__arr[self.__size-1] = None
        self.__size -= 1

        if self.__size <= self.__capacity / 4:
            self.__shrink()

    def display(self):
        print(f"Cap: {self.__capacity} Size: {self.__size} Values: {self.__arr}")

