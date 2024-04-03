import logging

# Configure logging to write to a file with current time
log_file = 'terminal_input.log'
logging.basicConfig(
    level=logging.INFO,
    filename=log_file,
    filemode='w',  # 'w' to overwrite the file
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)

def log_input(input_text):
    logging.info(f"User Input: {input_text}")

if __name__ == "__main__":
    print("This program logs all inputs. Type 'exit' to stop.")

    while True:
        user_input = input("Enter something: ")
        log_input(user_input)

        if user_input.lower() == 'exit':
            break

    print("Program terminated. Check the log file for inputs.")
