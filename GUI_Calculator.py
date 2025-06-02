from tkinter import *

first_num = second_num = symbol = None

root = Tk()

def digit(d):
    current = input_label['text']
    new = current + str(d)
    input_label.config(text=new)

def clear():
    input_label.config(text='')

def operator(op):
    global first_num, symbol
    first_num = int(input_label['text']) if input_label['text'] else 0
    symbol = op
    input_label.config(text='')

def equal_to():
    global first_num, second_num, symbol
    try:
        second_num = int(input_label['text'])
        if symbol == '+':
            input_label.config(text=str(first_num + second_num))
        elif symbol == '-':
            input_label.config(text=str(first_num - second_num))
        elif symbol == '*':
            input_label.config(text=str(first_num * second_num))
        elif symbol == '/':
            if second_num == 0:
                input_label.config(text="Error: Division by 0")
            else:
                input_label.config(text=str(first_num / second_num))
    except:
        input_label.config(text="Error")

root.geometry('375x490')
root.resizable(0, 0)
root.config(bg='pink')

input_label = Label(text='', fg='black', bg='pink', anchor='e')
input_label.grid(row=0, column=0, columnspan=4, pady=(50, 20), sticky='we')
input_label.config(font=("Helvetica", 40, "bold", "italic"))


for i in range(5):
    root.grid_rowconfigure(i, weight=1)
for j in range(4):
    root.grid_columnconfigure(j, weight=1) 

Button(text='7', fg='pink', bg='black', command=lambda: digit(7), font='Didone').grid(row=1, column=0, sticky='nsew')
Button(text='8', fg='pink', bg='black', command=lambda: digit(8), font='Didone').grid(row=1, column=1, sticky='nsew')
Button(text='9', fg='pink', bg='black', command=lambda: digit(9), font='Didone').grid(row=1, column=2, sticky='nsew')
Button(text='+', fg='pink', bg='black', command=lambda: operator('+'), font='Didone').grid(row=1, column=3, sticky='nsew')

Button(text='6', fg='pink', bg='black', command=lambda: digit(6), font='Didone').grid(row=2, column=0, sticky='nsew')
Button(text='5', fg='pink', bg='black', command=lambda: digit(5), font='Didone').grid(row=2, column=1, sticky='nsew')
Button(text='4', fg='pink', bg='black', command=lambda: digit(4), font='Didone').grid(row=2, column=2, sticky='nsew')
Button(text='-', fg='pink', bg='black', command=lambda: operator('-'), font='Didone').grid(row=2, column=3, sticky='nsew')

Button(text='3', fg='pink', bg='black', command=lambda: digit(3), font='Didone').grid(row=3, column=0, sticky='nsew')
Button(text='2', fg='pink', bg='black', command=lambda: digit(2), font='Didone').grid(row=3, column=1, sticky='nsew')
Button(text='1', fg='pink', bg='black', command=lambda: digit(1), font='Didone').grid(row=3, column=2, sticky='nsew')
Button(text='*', fg='pink', bg='black', command=lambda: operator('*'), font='Didone').grid(row=3, column=3, sticky='nsew')

Button(text='clear', fg='pink', bg='black', command=clear, font='Didone').grid(row=4, column=0, sticky='nsew')
Button(text='0', fg='pink', bg='black', command=lambda: digit(0), font='Didone').grid(row=4, column=1, sticky='nsew')
Button(text='=', fg='pink', bg='black', command=equal_to, font='Didone').grid(row=4, column=2, sticky='nsew')
Button(text='/', fg='pink', bg='black', command=lambda: operator('/'), font='Didone').grid(row=4, column=3, sticky='nsew')

root.mainloop()
