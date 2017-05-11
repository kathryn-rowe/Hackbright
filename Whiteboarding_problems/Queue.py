class Queue(object):
    """generic queue implementation"""

    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.append(item)

    # def enqueue(self, item):
    #     self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop(0)

    # def dequeue(self):
    #     return self.items.pop()

    def size(self):
        return len(self.items)
