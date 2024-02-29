# 2. Create 3 decorators for cleaning strings/text. The first decorator should remove trailing whitespace in the string.
# The second decorator should change all spaces into underscores. The third decorator should change text into lowercase.
# Apply all three of these decorators to a function which asks input from a user.
# For example:
# >>> prompt_user()
# >>> John ate an Apple    # this is what the user types in
# john_ate_an_apple        # this is the output of the function

def remove_trailing_whitespace(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.strip()
    return wrapper

def replace_spaces_with_underscores(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.replace(' ', '_')
    return wrapper

def lowercase(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        return result.lower()
    return wrapper
@remove_trailing_whitespace
@replace_spaces_with_underscores
@lowercase
def prompt_user():
    return input(">>> ")

# Call the function
result = prompt_user()
print(result)
