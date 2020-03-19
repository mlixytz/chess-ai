from tkinter import Tk, Canvas, PhotoImage, mainloop

WIDTH, HEIGHT = 530, 580
start_x, start_y = 37, 37


tk = Tk()

canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()

# 棋盘
img = PhotoImage(file='./img/bg.png')
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state='normal')

# 棋子
# 车
vehicle = PhotoImage(file = "./img/b_c.png")
image = canvas.create_image((start_x, start_y), image=vehicle)

# 马
horse = PhotoImage(file = "./img/b_c.png")
image = canvas.create_image((2 * start_x + 20, start_y), image=horse)

# 象
elephant = PhotoImage(file = "./img/b_c.png")
image = canvas.create_image((3 * start_x + 40, start_y), image=elephant)
 
# 士
guarder = PhotoImage(file = "./img/b_c.png")
image = canvas.create_image(((4 * start_x + 60, start_y)), image=guarder)
# vehicle = PhotoImage(file = "./img/b_c.png")
# image = canvas.create_image((37, 37), image=vehicle)

# vehicle = PhotoImage(file = "./img/b_c.png")
# image = canvas.create_image((37, 37), image=vehicle)

# vehicle = PhotoImage(file = "./img/b_c.png")
# image = canvas.create_image((37, 37), image=vehicle)

# vehicle = PhotoImage(file = "./img/b_c.png")
# image = canvas.create_image((37, 37), image=vehicle)


# vehicle = PhotoImage(file = "./img/b_c.png")
# image = canvas.create_image((37, 37), image=vehicle)

# vehicle = PhotoImage(file = "./img/b_c.png")
# image = canvas.create_image((37, 37), image=vehicle)


# vehicle = PhotoImage(file = "./img/b_c.png")
# image = canvas.create_image((37, 37), image=vehicle)


# vehicle = PhotoImage(file = "./img/b_c.png")
# image = canvas.create_image((37, 37), image=vehicle)

# vehicle = PhotoImage(file = "./img/b_c.png")
# image = canvas.create_image((37, 37), image=vehicle)


tk.mainloop()