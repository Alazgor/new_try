class MathOperations:
    @classmethod
    def is_prime(cls, num: int) -> bool:
        if num <= 1:
            return False
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                return False
        return True

    @classmethod
    def generate_primes(cls, n: int) -> list[int]:
        prime_numbers = []
        for num in range(2, n + 1):
            if cls.is_prime(num):
                prime_numbers.append(num)
        return prime_numbers

# Example usage:
primes_up_to_20 = MathOperations.generate_primes(20)
print(primes_up_to_20)  # Output: [2, 3, 5, 7, 11, 13, 17, 19]
