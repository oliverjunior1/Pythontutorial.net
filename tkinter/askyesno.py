# import tkinter as tk
# from tkinter import ttk
# from tkinter.messagebox import askyesno

# root = tk.Tk()
# root.title('Tkinter Yes/No Dialog')
# root.geometry('300x150')

# def confirm():
#     answer = askyesno(title='confirmation', message='Are you sure that you want to quit?')
#     if answer:
#         root.destroy()
    
# ttk.Button(
#     root,
#     text='Ask Yes/No',
#     command=confirm).pack(expand=True)

# root.mainloop()

#####################################

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import askyesno, askquestion

class App(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title('Tkinter Yes/Bi Dialog')
        self.geometry('300x150')

        quit_button = ttk.Button(self, text='Quit', command=self.confirm)
        quit_button.pack(expand = True)

    def confirm(self):
        answer = askyesno(title='Confirmation', message='Are you sure that you want to quit?')

        if answer:
            self.destroy()

if __name__ == '__main__':
    app = App()
    app.mainloop()