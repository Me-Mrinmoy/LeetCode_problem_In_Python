class MyCircularQueue:

    def __init__(self, k):
        self.queue = [0] * k      # fixed-size array
        self.size = k             # max capacity
        self.front = 0            # front pointer
        self.rear = 0             # rear pointer
        self.count = 0            # current number of elements

    def enQueue(self, value):
        if self.isFull():
            return False
        self.queue[self.rear] = value
        self.rear = (self.rear + 1) % self.size
        self.count += 1
        return True

    def deQueue(self):
        if self.isEmpty():
            return False
        self.front = (self.front + 1) % self.size
        self.count -= 1
        return True

    def Front(self):
        if self.isEmpty():
            return -1
        return self.queue[self.front]

    def Rear(self):
        if self.isEmpty():
            return -1
        return self.queue[(self.rear - 1 + self.size) % self.size]

    def isEmpty(self):
        return self.count == 0

    def isFull(self):
        return self.count == self.size
