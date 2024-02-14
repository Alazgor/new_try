# import logging
#
# # Configure logging to write to a file with current time
# log_file = 'data.log'
# logging.basicConfig(
#     level=logging.DEBUG,
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     datefmt='%d/%m/%Y %H:%M:%S',  # Corrected format
#     handlers=[
#         logging.FileHandler(log_file, mode='w'),  # 'w' to overwrite the file
#         logging.StreamHandler()  # Log to console as well
#     ]
# )
#
# # Log messages
# logging.debug('This is Debug Message')
# logging.info('This is an info message')

import logging

logging.basicConfig(
    level=logging.DEBUG,
    filename='data.log',
    filemode='w',  # 'w' to overwrite the file each time
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)

name = input("Enter Your Name:\n")
logging.info(f"{name} has logged in successfully !!")

# Additional code with exception handling
a = 10
b = 0
try:
    c = a / b
except Exception as e:
    logging.error("Exception Occurred", exc_info=True)



