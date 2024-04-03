class A:
    def __init__(self, value):
        self.value = value

    def increment(self):
        self.value += 1

class B(A):
    def __init__(self, value, step):
        super().__init__(value)
        self.step = step

    def increment(self):
        # super().increment()
        self.value += self.step

b = B(5, 3)
b.increment()
print(b.value)
