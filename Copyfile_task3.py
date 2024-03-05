import os
from datetime import datetime

# Function to create a directory on the desktop
def create_directory(directory_name):
    desktop_path = os.path.join(os.path.expanduser("~"), "C:\\Users\\aleks\\CodeAcademy\\pythonProject")
    directory_path = os.path.join(desktop_path, directory_name)
    os.makedirs(directory_path, exist_ok=True)
    return directory_path

# Function to create a text file with today's date and time
def create_text_file(directory_path):
    file_name = datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
    file_path = os.path.join(directory_path, file_name)
    with open(file_path, 'w') as file:
        file.write("Creation date and time: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
    return file_path

# Function to print creation date and size of the text file
def print_file_info(file_path):
    file_stat = os.stat(file_path)
    creation_time = datetime.fromtimestamp(file_stat.st_ctime)
    file_size = file_stat.st_size
    print(f"Creation date: {creation_time}")
    print(f"Size: {file_size} bytes")

# Main function
def main():
    directory_name = "PythonProject_New"
    directory_path = create_directory(directory_name)
    file_path = create_text_file(directory_path)
    print("Text file created successfully.")
    print_file_info(file_path)

if __name__ == "__main__":
    main()
