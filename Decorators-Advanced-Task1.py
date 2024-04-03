# 1. Write a decorator that decorates a string-returning function in an email style. For example: write_email
# ("this is some text") should return
# "To whom it may concern, this is some text Sincerely,Sender"

def email_style(func):
    def wrapper(*args, **kwargs):
        text = func(*args, **kwargs)
        return f"To whom it may concern, {text} Sincerely, Sender"
    return wrapper

@email_style
def write_email(text):
    return text

# Example usage
result = write_email("this is some text")
print(result)
