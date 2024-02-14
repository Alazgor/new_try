i = 0

# while i < 10:
#     print(i)
#     i +=1

while True:
    user_input = input("Enter your name: ")
    if len(user_input) > 0:
        break

print(f"You entered {user_input}")

while True:
    secret = "secret"
    user_input = input("Enter the secret: ")
    if user_input == secret:
        print("You're in!")
        break
    else:
        print("Sorry, try again!")
