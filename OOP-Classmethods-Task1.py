class MathOperations:
    @classmethod
    def factorial(cls, n: int) -> int:
        if n == 0:
            return 1
        else:
            return n * cls.factorial(n-1)

print(MathOperations.factorial(5)) # Output: 120
