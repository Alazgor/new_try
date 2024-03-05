import this
import os
import re
from datetime import datetime

# Функция для добавления даты и времени в последнюю строку файла
def add_date_time(file_name):
    with open(file_name, 'a') as file:
        file.write("\nDate and time: " + datetime.now().strftime("%Y-%m-%d %H:%M:%S"))

# Функция для замены первой вхождения фразы в файле
def replace_first_occurrence(file_name, old_text, new_text):
    with open(file_name, 'r+') as file:
        content = file.read()
        file.seek(0)
        file.write(content.replace(old_text, new_text, 1))

# Функция для вывода текста файла в обратном порядке
def print_reverse(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
        print(text[::-1])

# Функция для подсчета слов, чисел, заглавных и строчных букв в тексте файла
def count_chars(file_name):
    with open(file_name, 'r') as file:
        text = file.read()
        words = len(re.findall(r'\b\w+\b', text))
        numbers = len(re.findall(r'\d+', text))
        uppercase = sum(1 for char in text if char.isupper())
        lowercase = sum(1 for char in text if char.islower())
        print(f"Words: {words}\nNumbers: {numbers}\nUppercase: {uppercase}\nLowercase: {lowercase}")

# Функция для копирования текста файла в новый файл, только прописными буквами
def copy_to_uppercase(file_name, new_file_name):
    with open(file_name, 'r') as file:
        text = file.read()
    with open(new_file_name, 'w') as new_file:
        new_file.write(text.upper())

# Создание исходного файла с текстом из "import this"
with open("Text.txt", 'w') as file:
    import this
    add_date_time("Text.txt")

# Печать текста из созданного файла
print("Text from created file:")
with open("Text.txt", 'r') as file:
    for i, line in enumerate(file, start=1):
        print(f"{i}. {line.strip()}")

# Добавление сегодняшней даты и времени в последнюю строку
add_date_time("Text.txt")

# Добавление номеров к строкам
with open("Text.txt", 'r+') as file:
    lines = file.readlines()
    file.seek(0)
    for i, line in enumerate(lines, start=1):
        file.write(f"{i}. {line}")

# Замена строки "Красивое лучше, чем уродливое"
replace_first_occurrence("Text.txt", "Красивое лучше, чем уродливое", "Beautiful is better than ugly.")

# Вывод текста файла в обратном порядке
print("\nText from created file in reverse:")
print_reverse("Text.txt")

# Вывод количества слов, чисел, заглавных и строчных букв
print("\nCounts:")
count_chars("Text.txt")

# Копирование текста файла в новый файл, только прописными буквами
copy_to_uppercase("Text.txt", "Uppercase_Text.txt")
