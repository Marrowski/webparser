from tkinter import *
from tkinter import ttk

import requests

root = Tk()
root.title('Парсер веб-застосунків')
root.geometry('1000x800')


label = Label(text='Вітаю у парсері!')
label1 = Label(text='Введіть у текстове поле нижче адресу для парсингу.')
label.pack()
label1.pack()


root.mainloop()