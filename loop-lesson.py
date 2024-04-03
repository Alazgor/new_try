correct_username = "Aliaksei"
correct_password = "secret"
max_attempts = 3
attempts = 0

while attempts < max_attempts:
    username = input("Enter your username: ")
    password = input("Enter your password: ")

    if username == correct_username and password == correct_password:
        print("You In!")
        break
    else:
        attempts += 1
        remaining_attempts = max_attempts - attempts
        print(f"Try again. Incorrect username or password. Remaining attempts: {remaining_attempts}")

if attempts == max_attempts:
    print("Sorry, you've reached the maximum number of attempts. Access denied.")
