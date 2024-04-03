import logging

# Configure logging to write to a file with current time
log_file = 'move_to_end.log'
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S',
    handlers=[
        logging.FileHandler(log_file, mode='w'),  # 'w' to overwrite the file
        logging.StreamHandler()  # Log to console as well
    ]
)

logging.debug('This is Debug Message')

lst = [1, 2, 2.5, 'a']

def are_all_numbers(lst: list):
    for i in lst:
        logging.debug(f'{i}, {type(i)}')
        if not isinstance(i, (int, float)):  # Check if i is not an integer or not a float
            logging.info(f'{i} is not a number: {type(i)}')
            return False
    logging.info('All elements are numbers')
    return True

def ten_el_long(lst):
    if are_all_numbers(lst):
        logging.info(f'The list length is {len(lst)}')
        if len(lst) < 10:
            return False
        logging.info(f'The list length is greater than 10')
        return True
    return False

def sort_list(lst):
    if ten_el_long(lst):
        return sorted(lst)
    logging.error(f'The list is less than 10 elements long')

print(ten_el_long(lst))
print(sort_list(lst))


# import logging
#
# # Configure logging to write to a file with current time
# log_file = 'car_operations.log'
# logging.basicConfig(
#     level=logging.DEBUG,
#     filename=log_file,
#     filemode='w',  # 'w' to overwrite the file
#     format='%(asctime)s - %(levelname)s - %(message)s',
#     datefmt='%d/%m/%Y %H:%M:%S'
# )
#
#
# def check_engine() -> None:
#     logging.debug("Checking status of engine...")
#
#     # Simulate checking engine conditions
#     engine_status = True
#
#     if engine_status:
#         logging.info("Engine is in good condition.")
#     else:
#         logging.warning("Engine needs attention.")
#
#
# def start_car() -> None:
#     logging.debug("Starting car...")
#
#     try:
#         # Attempt to start the car by checking the engine
#         check_engine()
#
#         # Simulate starting the car
#         logging.info("Car started successfully.")
#
#     except Exception as e:
#         logging.error(f"Error occurred while starting car: {e}")
#
#
# def drive_car() -> None:
#     logging.debug("Driving car...")
#
#     try:
#         # Attempt to drive the car by starting it
#         start_car()
#
#         # Simulate driving the car
#         logging.info("Car is now in motion.")
#
#     except Exception as e:
#         logging.error(f"Error occurred while driving car: {e}")
#
#
# if __name__ == "__main__":
#     # Testing different logging severity levels
#     drive_car()
