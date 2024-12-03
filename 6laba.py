import os
from random import randint
from tkinter import Tk, Button, Label, Entry, messagebox, StringVar
from tkinter.filedialog import askopenfilename

# Функция для генерации файла с числами
def generate():
    file_name = askopenfilename(defaultextension=".txt", filetypes=[("Text files", ".txt"), ("All files", "*.*")])
    if not file_name:
        messagebox.showinfo("Info", "Файл не выбран")
        return

    # Генерация файла с случайными числами
    with open(file_name, 'w') as temp_file:
        for i in range(10):
            temp_file.write(str(randint(1, 50)) + " ")

    # Чтение содержимого файла
    with open(file_name, 'r') as temp_file:
        content = temp_file.read()
        output.set("Содержимое: " + content)
        numbers = list(map(int, content.split()))
        if numbers:
            average = sum(numbers) / len(numbers)
            output.set(output.get() + f"\nСр. значение: {average}")
        else:
            output.set(output.get() + "\nФайл пуст")

# Функция для выполнения математических операций
def math_operations():
    try:
        a = int(entry_a.get())
        b = int(entry_b.get())

        results = [
            f'{a} + {b} = {a + b}',
            f'{a} - {b} = {a - b}',
            f'{a} * {b} = {a * b}'
        ]

        if b != 0:
            results.append(f'{a} / {b} = {a / b}')
        else:
            results.append("Деление на 0 невозможно")

        output.set("\n".join(results))
    except ValueError:
        output.set("Пожалуйста, введите действительные числа.")

# Настройка графического интерфейса
root = Tk()
root.configure(bg='lightblue')
root.title("laba6")
root.geometry("500x400")

# Переменная для вывода результатов
output = StringVar()
output_label = Label(root, textvariable=output, wraplength=400)
output_label.pack(pady=20)

# Кнопка для генерации чисел
Button(root, text="Генерировать числа", command=generate).pack(pady=5)

# Поле ввода для первого числа
Label(root, text="Первое число:").pack()
entry_a = Entry(root)
entry_a.pack(pady=5)

# Поле ввода для второго числа
Label(root, text="Второе число:").pack()
entry_b = Entry(root)
entry_b.pack(pady=5)

# Кнопка для выполнения математических операций
Button(root, text="Выполнить математические операции", command=math_operations).pack(pady=20)

# Запуск основного цикла программы
root.mainloop()
