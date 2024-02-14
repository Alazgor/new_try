import logging

# Configure logging to write to a file with current time
log_file = 'data_input.log'
logging.basicConfig(
    level=logging.DEBUG,
    filename=log_file,
    filemode='w',  # 'w' to overwrite the file
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)

def process_input(user_input):
    try:
        if isinstance(user_input, str):
            logging.info(f"Entered data type: string - Value: {user_input}")
        elif isinstance(user_input, (int, float)):
            logging.info(f"Entered data type: number - Value: {user_input}")
        elif isinstance(user_input, list):
            logging.info(f"Entered data type: list - Value: {user_input}")
        elif isinstance(user_input, dict):
            logging.info(f"Entered data type: dict - Value: {user_input}")
        else:
            logging.warning(f"Unexpected data type: {type(user_input)} - Value: {user_input}")

    except Exception as e:
        logging.error(f"Error processing input: {e}")

if __name__ == "__main__":
    for _ in range(10):
        try:
            user_input = eval(input("Enter data: "))  # Using eval to evaluate different data types
            process_input(user_input)

        except KeyboardInterrupt:
            logging.error("Program terminated by user.")
            break

        except Exception as e:
            logging.error(f"Error processing input: {e}")

    logging.info("Program finished.")
