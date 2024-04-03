class User:
    def __init__(self, username):
        self.username = username
        self._password = None

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, value):
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        if not any(char.isupper() for char in value):
            raise ValueError("Password must contain at least one uppercase letter.")
        if not any(char.islower() for char in value):
            raise ValueError("Password must contain at least one lowercase letter.")
        if not any(char.isdigit() for char in value):
            raise ValueError("Password must contain at least one digit.")
        self._password = value

# Example usage:
user = User("john_doe")

# Set a strong password
user.password = "StrongPassword123"
print("Password set successfully.")

# Try setting a weak password
try:
    user.password = "weak"
except ValueError as e:
    print("Error:", e)
