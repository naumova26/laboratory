import os
import tkinter as tk
from tkinter import filedialog
import random

def create_file_with_random_numbers(fileName, count):
    with open(fileName, 'w+') as file:
        for i in range(count):
            number = random.randint(1, 25)
            file.write(f"{number}\n")

#поменять путь
fileName = "C:/Users/error/Desktop/labort/random_numbers.txt"
count = 10

create_file_with_random_numbers(fileName, count)
print(f"Создан файл {fileName} с {count} случайными числами.")

def create_file_with_random_numbers(fileName, count):
    with open(fileName, 'w+') as file:
        for i in range(count):
            number = random.randint(1, 25)
            file.write(f"{number}\n")

#поменять путь
fileName = "C:/Users/error/Desktop/labort/random_numbers.txt"
count = 10

create_file_with_random_numbers(fileName, count)
print(f"Создан файл {fileName} с {count} случайными числами.")

def create_file_with_random_numbers(fileName, count):
    with open(fileName, 'w+') as file:
        for i in range(count):
            number = random.randint(1, 25)
            file.write(f"{number}\n")

#поменять путь
fileName = "C:/Users/error/Desktop/labort/random_numbers.txt"
count = 10

create_file_with_random_numbers(fileName, count)
print(f"Создан файл {fileName} с {count} случайными числами.")

# Выбор файла с помощью диалогового окна
def choose_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(
        initialdir="/",
        title="Выберите файл",
        filetypes=(("Text Files", "*.txt"), ("All Files", "*.*"))
    )
    return file_path


def write_to_file(file_name, content):
    with open(file_name, 'a', encoding='utf-8') as file:
        file.write(content + "\n")
    print(f"Запись в файл {file_name} завершена.")

def read_from_file(file_name):
    if os.path.exists(file_name):
        with open(file_name, 'r', encoding='utf-8') as file:
            content = file.readlines()
            print(f"Содержимое файла {file_name}:")
            for line in content:
                print(line.strip())
    else:
        print(f"Файл {file_name} не существует.")

if __name__ == "__main__":  
    print("Выберите файл для чтения и записи:")
    selected_file = choose_file()

    if selected_file:
        write_to_file(selected_file, "Добавленный текст") 
        read_from_file(selected_file)
    else:
        print("Файл не был выбран.")

with open(fileName, 'r') as file:
    numbers = [int(line.strip()) for line in file.readlines()]

average = sum(numbers) / len(numbers) if numbers else 0
print("Среднее значение чисел:", average)
