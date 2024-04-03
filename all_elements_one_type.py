import logging

# Configure logging to write to a file with current time
log_file = 'move_to_end.log'
logging.basicConfig(
    level=logging.INFO,
    filename=log_file,
    filemode='w',  # 'w' to overwrite the file
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d/%m/%Y %H:%M:%S'
)

def move_to_end(lst, element):
    logging.info(f"Input List: {lst}")
    logging.info(f"Element to Move to End: {element}")

    try:
        # Move all occurrences of the element to the end of the list
        for _ in range(lst.count(element)):
            lst.remove(element)
            lst.append(element)

        logging.info(f"Result List: {lst}")
        return lst

    except Exception as e:
        logging.error(f"Error occurred: {e}")
        return None

if __name__ == "__main__":
    example_list = [1, 3, 2, 4, 4, 1]
    element_to_move = 1

    result = move_to_end(example_list, element_to_move)

    print(f"Original List: {example_list}")
    print(f"Element to Move to End: {element_to_move}")
    print(f"Result List: {result}")
