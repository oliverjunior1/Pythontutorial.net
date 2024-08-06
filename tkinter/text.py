# from tkinter import Tk, Text

# root= Tk()
# root.resizable(False, False)
# root.title('Text Widget Example')

# text = Text(root, height=5)
# text.pack()

# root.mainloop()

#####################################

from tkinter import Tk, Text

root = Tk()
root.resizable(False, False)
root.title('Text Widget Example')

text = Text(root, height=8)
text.pack()

text.insert('1.0', 'This is a Text Widged demo')

root.mainloop()


