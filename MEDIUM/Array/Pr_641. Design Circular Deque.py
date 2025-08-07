class MyCircularDeque:
    def __init__(self, k):
        self.capacity = k + 1  # Extra space to distinguish full from empty
        self.data = [0] * self.capacity
        self.front = 0
        self.rear = 0

    def insertFront(self, value):
        if self.isFull():
            return False
        self.front = (self.front - 1 + self.capacity) % self.capacity
        self.data[self.front] = value
        return True

    def insertLast(self, value):
        if self.isFull():
            return False
        self.data[self.rear] = value
        self.rear = (self.rear + 1) % self.capacity
        return True

    def deleteFront(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.capacity
        return True

    def deleteLast(self):
        if self.isEmpty():
            return False
        self.rear = (self.rear - 1 + self.capacity) % self.capacity
        return True

    def getFront(self):
        if self.isEmpty():
            return -1
        return self.data[self.front]

    def getRear(self):
        if self.isEmpty():
            return -1
        return self.data[(self.rear - 1 + self.capacity) % self.capacity]

    def isEmpty(self):
        return self.front == self.rear

    def isFull(self):
        return (self.rear + 1) % self.capacity == self.front
