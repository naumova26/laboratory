import os
from random import randint
from tkinter import Tk, Button, Label, Entry, messagebox, StringVar
from tkinter.filedialog import askopenfilename

def generate():
    file_name = askopenfilename(defaultextension=".txt", filetypes=[("Text files", ".txt"), ("All files", "*.*")])
    if not file_name:
        messagebox.showinfo("Info", "Файл не выбран")
        return

    with open(file_name, 'w') as temp_file:
        for i in range(10):
            temp_file.write(str(randint(1, 50)) + " ")

    with open(file_name, 'r') as temp_file:
        content = temp_file.read()
        output.set("Содержимое файла: \n" + content)
        numbers = list(map(int, content.split()))
        if numbers:
            average = sum(numbers) / len(numbers)
            output.set(output.get() + f"\nСреднее значение: {average:.2f}")
        else:
            output.set(output.get() + "\nФайл пуст")

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
            results.append(f'{a} / {b} = {a / b:.2f}')
        else:
            results.append("Деление на 0 невозможно")

        output.set("\n".join(results))
    except ValueError:
        output.set("Ошибка: Пожалуйста, введите действительные числа.")

def clear():
    entry_a.delete(0, 'end')
    entry_b.delete(0, 'end')
    output.set("")

root = Tk()
root.configure(bg='lightblue')
root.title("Лабораторная работа 6")
root.geometry("500x500")

output = StringVar()
output_label = Label(root, textvariable=output, wraplength=400, bg='lightyellow', relief="sunken", width=50, height=6)
output_label.pack(pady=20)

Button(root, text="Генерировать числа", command=generate, bg='lightgreen').pack(pady=5)
Label(root, text="Первое число:", bg='lightblue').pack()
entry_a = Entry(root)
entry_a.pack(pady=5)

Label(root, text="Второе число:", bg='lightblue').pack()
entry_b = Entry(root)
entry_b.pack(pady=5)

Button(root, text="Выполнить операции", command=math_operations, bg='lightcoral').pack(pady=20)
Button(root, text="Очистить", command=clear, bg='lightgrey').pack(pady=5)

root.mainloop()
