# 6. Create 3 decorators for cleaning strings/text. The first decorator should remove trailing whitespace in the string.
# The second decorator should change all spaces into underscores. The third decorator should change text into lowercase.
# Apply all three of these decorators to a function which asks input from a user. For example:
# >>> prompt_user()
# >>> John ate an Apple    # this is what the user types in
# >>> john_ate_an_apple

# Remove trailing whitespace:

def remove_trailing_whitespace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.strip()
    return wrapper
# Change spaces into underscores:

def replace_spaces_with_underscores(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.replace(' ', '_')
    return wrapper
# Change text into lowercase:

def convert_to_lowercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.lower()
    return wrapper

@remove_trailing_whitespace
@replace_spaces_with_underscores
@convert_to_lowercase
def prompt_user():
    return input(">>> ")

# Test the implementation
cleaned_text = prompt_user()
print(cleaned_text)