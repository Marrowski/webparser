import tkinter as tk
from tkinter import *
import requests

class ParserApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Парсер веб-застосунків')
        self.geometry('1000x1000')
        
        self.label = tk.Label(text='Вітаю у парсері!', font=('Arial', 18), fg='blue')
        self.label1 = tk.Label(text='Введіть у текстове поле нижче адресу для парсингу', font=('Arial', 18), fg='red')
        self.link = tk.Entry(self, width=50)
        
        self.button = tk.Button(text='Дістати дані', command=self.parse_data)
        
        self.label.pack()
        self.label1.pack()
        
        self.link.pack(anchor='n', padx=20, pady=20)
        
        self.button.pack()
        
        self.var = IntVar()
        self.var.set(0)
        
        self.c1 = tk.Radiobutton(text='GET', variable=self.var, val=0)
        self.c2 = tk.Radiobutton(text='POST', variable=self.var, val=1)
        self.c3 = tk.Radiobutton(text='PUT', variable=self.var, val=2)
        self.c4 = tk.Radiobutton(text='DELETE', variable=self.var, val=3)
        
        self.c1.pack()
        self.c2.pack()
        self.c3.pack()
        self.c4.pack()
        
        self.text = Text(width=50, height=10)
        self.text.pack()
        
        self.payload_text = tk.Label(text='Payload(Якщо запит POST або PUT)')
        self.payload_text.pack()
        
        self.payload = tk.Text(width=50, height=3)
        self.payload.pack()
        
    def parse_data(self):
        self.input_text = self.link.get()
        try:
            if self.var.get() == 0:
                self.data = requests.get(self.input_text)
                self.text.insert(tk.END, self.data.text)
                
            elif self.var.get()  == 1:
                self.data = requests.post()
            elif self.var.get()  == 2:
                self.data = requests.put()
            elif self.var.get() == 3:
                self.data = requests.delete()
        except requests.RequestException as e:
            self.text.insert(tk.END, e)
            
    
            
        


if __name__ == '__main__':
    app = ParserApp()
    app.mainloop()