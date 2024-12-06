import tkinter as tk
from distutils.command.config import config


def get_values():
    num1 = int(number1_entry.get())
    num2 = int(number2_entry.get())
    return  num1, num2


def insert_values(value):
    answer_entry.delete(0, 'end')
    answer_entry.insert(0, value)


def add():
    num1, num2 = get_values()
    res = num1 + num2
    insert_values(res)


def sub():
    num1, num2 = get_values()
    res = num1 - num2
    insert_values(res)


def mul():
    num1, num2 = get_values()
    res = num1 * num2
    insert_values(res)


def div():
    num1, num2 = get_values()
    res = num1 / num2
    insert_values(res)


def per():
    num1, num2 = get_values()
    res = (num1 * 100) / num2
    insert_values(res)

window = tk.Tk()
window.title('КАЛЬКУЛЯТОР')
window.geometry("290x300")
window.configure(bg='lightblue')
window.resizable(False,False)
button_add = tk.Button(window, text="+", font=('Arial', '14'), width=2, height=1, command=add)
button_add.place(x=48, y=170)
button_add.configure(bg='blue', activebackground='white')
button_sub = tk.Button(window, text="-",font=('Arial', '14'), width=2, height=1, command=sub)
button_sub.place(x=88, y=170)
button_sub.configure(bg='red',activebackground='white')
button_mul = tk.Button(window, text="*", font=('Arial', '14'), width=2, height=1, command=mul)
button_mul.place(x=128, y=170)
button_mul.configure(bg='lightgrey', activebackground='white')
button_div = tk.Button(window, text="/", font=('Arial', '14'), width=2, height=1, command=div)
button_div.place(x=168, y=170)
button_div.configure(bg='magenta', activebackground='white')
button_per = tk.Button(window, text="%", font=('Arial', '14'), width=2, height=1, command=per)
button_per.place(x=208, y=170)
button_per.configure(bg='steelblue', activebackground='white')
number1_entry = tk.Entry(window, width=17, font=('Arial', 14))
number1_entry.place(x=50, y=50)
number1 = tk.Label(window, text="ВВЕДИТЕ ПЕРВОЕ ЧИСЛО", fg='darkblue')
number1.place(x=75, y=28)
number2_entry = tk.Entry(window, width=17, font=('Arial', 14))
number2_entry.place(x=50, y=120)
number2 = tk.Label(window, text="ВВЕДИТЕ ВТОРОЕ ЧИСЛО", fg='darkblue')
number2.place(x=75, y=98)
answer_entry = tk.Entry(window, width=17, font=('Arial', 14))
answer_entry.place(x=50, y=250)
answer = tk.Label(window, text="РЕЗУЛЬТАТ", fg='darkblue')
answer.place(x=110, y=228)

window.mainloop()