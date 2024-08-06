# import tkinter as tk
# from tkinter import ttk

# root = tk.Tk()
# root.geometry('240x100')
# root.title('Login')
# root.resizable(0,0)

# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=3)

# username_label = ttk.Label(root, text='Username:')
# username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

# username_entry = ttk.Entry(root)
# username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

# password_label = ttk.Label(root, text='Password:')
# password_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

# password_entry = ttk.Entry(root, show='*')
# password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

# login_button = ttk.Button(root, text='Login')
# login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

# root.mainloop()
##################################################

import tkinter as tk
from tkinter import ttk

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.geometry('240x100')
        self.title('Login')
        self.resizable(0,0)

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=3)

        self.create_widgets()

    def create_widgets(self):
        username_label = ttk.Label(self, text='Username:')
        username_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        username_entry = ttk.Entry(self)
        username_entry.grid(column=1, row=0, sticky=tk.E, padx=5, pady=5)

        password_label = ttk.Label(self, text='Password:')
        password_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

        password_entry = ttk.Entry(self, show='*')
        password_entry.grid(column=1, row=1, sticky=tk.E, padx=5, pady=5)

        login_button= ttk.Button(self, text='Login')
        login_button.grid(column=1, row=3, sticky=tk.E, padx=5, pady=5)

if __name__ == '__main__':
    app = App()
    app.mainloop()
