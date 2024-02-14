class MyQueue:
    def __init__(self):
        self.items = []

    def __bool__(self):
        return bool(self.items)

    def __repr__(self):
        return f"MyQueue({self.items})"

    def __len__(self):
        return len(self.items)

# Example usage:
queue = MyQueue()
print(bool(queue))     # Output: False
print(len(queue))      # Output: 0
print(repr(queue))     # Output: MyQueue([])
queue.items.append(1)
queue.items.append(2)
queue.items.append(3)
print(bool(queue))     # Output: True
print(len(queue))      # Output: 3
print(repr(queue))     # Output: MyQueue([1, 2, 3])
