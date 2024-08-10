# import tkinter as tk

# root = tk.Tk()
# root.geometry('800x600')
# root.title('Canvas Demo - Oval')

# canvas = tk.Canvas(root, width=600, height=400, bg='white')
# canvas.pack(anchor=tk.CENTER, expand=True)

# points = (
#     (50, 150),
#     (200, 350),
# )
# canvas.create_oval(*points, fill='purple')

# root.mainloop()

#####################################
# import tkinter as tk

# root = tk.Tk()
# root.geometry('800x600')
# root.title('Canvas Demo - Rectangle')

# canvas = tk.Canvas(root, width=600, height=400, bg='white')
# canvas.pack(anchor=tk.CENTER, expand=True )

# canvas.create_rectangle((100,100),(300,300), fill='green')

# root.mainloop()

#####################################
# import tkinter as tk

# root = tk.Tk()
# root.geometry('800x600')
# root.title('Canvas Demo - Oval')

# canvas = tk.Canvas(root, width=600, height=400, bg='white')
# canvas.pack(anchor=tk.CENTER, expand=True)

# points = (
#     (50, 150),
#     (200,350),
# )
# canvas.create_oval(*points, fill='purple')

# root.mainloop()

#####################################
# import tkinter as tk

# root = tk.Tk()
# root.geometry('800x600')
# root.title('Canvas Demo - Poligon')

# canvas = tk.Canvas(root, width=600, height=400, bg='white')
# canvas.pack(anchor=tk.CENTER, expand=True)

# points = (
#     (100,300),
#     (200,200),
#     (300,300),
# )
# canvas.create_polygon(*points, fill='blue')

# root.mainloop()
#####################################
# import tkinter as tk

# root = tk.Tk()
# root.geometry('800x600')
# root.title('Canvas Demo - Text')

# canvas = tk.Canvas(root, width=600, height=400, bg='white')
# canvas.pack(anchor=tk.CENTER, expand=True)

# canvas.create_text(
#     (300,100),
#     text='Canvas Demo',
#     fill='Orange',
#     font='tkDefaeulFont 24'
# )

# root.mainloop()
#####################################
# import tkinter as tk
# from turtle import width

# root = tk.Tk()
# root.geometry('800x600')
# root.title('Canvas Demo - Arc')

# canvas = tk.Canvas(root, width=600, height=600, bg='white')
# canvas.pack(anchor=tk.CENTER, expand=True)

# canvas.create_arc((10,10),(200,200), style= tk.PIESLICE, width=2)
# canvas.create_arc((10,200),(200,390), style= tk.PIESLICE, width=2)
# canvas.create_arc((10,400),(200,590), style= tk.PIESLICE, width=2)

# root.mainloop()

#####################################
# import tkinter as tk

# root = tk.Tk()
# root.geometry('800x600')
# root.title('Canvas Demo - Image')

# canvas = tk.Canvas(root, width=600, height=400, bg='white')
# canvas.pack(anchor=tk.CENTER, expand=True)

# python_image = tk.PhotoImage(file='python.gif')
# canvas.create_image(
#     (100,100),
#     image=python_image
# )

# root.mainloop()
#####################################
import tkinter as tk

root = tk.Tk()
root.geometry('800x600')
root.title('Canvas Demo - Binding Event')

canvas = tk.Canvas(root, width=600, height=400, bg='white')
canvas.pack(anchor=tk.CENTER, expand=True)

python_image = tk.PhotoImage(file='Python.gif')
image_item = canvas.create_image(
    (100, 100),
    image = python_image
)
canvas.tag_bind(
    image_item,
    '<Button-1>',
    lambda e: canvas.delete(image_item)
)
root.mainloop()