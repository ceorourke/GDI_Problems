# tbh I don't think I solved this exactly right - I don't use
# 2 queues and didn't totally understand how to do that, so take
# this solution with a big grain of salt

class Queue(object):
    def __init__(self):
        self._data = []

    def first(self):
        """Look at the item at the front of the queue"""

        return self._data[0]

    def last(self):
        """Look at the item at the end of the queue"""

        return self._data[-1]

    def enqueue(self, item):
        """Add an item to the queue"""
        self._data.append(item)

    def dequeue(self):
        """Remove an item from the queue"""

        return self._data.pop(0)

    def is_empty(self):
        """Return whether the queue is empty or not"""

        return not self._data

class Stack(object):
    """A stack implemented using the Queue class"""

    def __init__(self):
        self.queue = Queue()

    def peek(self):
        return self.queue.first()

    def pop(self):
        if not self.is_empty:
            self.queue.dequeue()

    def push(self, item):
        self.queue.enqueue(item)

    def is_empty(self):
        return self.queue.is_empty()

astack = Stack()
print astack.is_empty() # true
astack.push("a")
print astack.peek() # "a"
print astack.is_empty() #false
astack.pop()
print astack.is_empty() #true
astack.pop()    