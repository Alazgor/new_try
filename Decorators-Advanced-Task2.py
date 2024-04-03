# 2. Write a decorator debug_mode that makes it clear that some text is for debugging and a function print_debug that would
# be decorated by this. For example, if I call print_debug("This should be 0") I would receive ("=== DEBUG: This should be "
# "0 ===") in the console
def debug_mode(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        debug_text = f"=== DEBUG: {text} ==="
        print(debug_text)
        return debug_text
    return wrapper

@debug_mode
def print_debug(text):
    return text

# Example usage
print_debug("This should be 0")
