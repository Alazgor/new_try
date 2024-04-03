class StringOperations:
    @classmethod
    def reverse_string(cls, input_string: str) -> str:
        return input_string[::-1]

# Example usage:
reversed_str = StringOperations.reverse_string("Hello world")
print(reversed_str)  # Output: "olleh"
