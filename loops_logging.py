import logging, logging.config

# set up logging
logging.config.fileConfig("logging.conf")
logger = logging.getLogger("sLogger")

# i = 1
#
# while i < 20:
#     print(i)
#     i *= 2
#
# while True:
#     print("hello")
#     print(i)
#     i += 1
#     if i > 10000:
#         break
#
# while True:
#     user_input = input("Enter your name: ")
#     if len(user_input) != 0:
#         break
#
# print(f"You entered {user_input}")

while True:
    secret = "secret"
    user_input = input("Enter the secret: ")
    logger.info(f"user entered: {user_input}")
    if user_input == secret:
        logger.info(f"user entered: {user_input} and got in")
        print("You're in!")
        break
    else:
        print("Sorry, try again!")