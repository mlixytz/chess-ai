from tkinter import Tk, Canvas, PhotoImage, mainloop, Button, Label

WIDTH, HEIGHT = 530, 580
start_x, start_y = 37, 39
space = 57

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)
canvas.pack()


def init():
    """ 棋盘初始化

        棋盘使用一维数组表示，大小为256，中间90个索引代表有效棋盘
        无效位置存储的值为-1，有效如果有子，用子对应的图片tag表示（大于0）
        如果无子用0表示。也就是 16 X 16 个格子，有效位置左上角坐标为（4， 4），
        右下角的坐标为（13， 12）
    """
    board = []
    start_row = start_col = 3
    end_row, end_col = 12, 11
    for i in range(256):
        pass

    # 创建图片
    pass




# 棋盘
img = PhotoImage(file='./img/bg.png')
canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state='normal')

# 棋子
# 车
vehicle = PhotoImage(file = "./img/b_j.png")
image1 = canvas.create_image((start_x, start_y), image=vehicle)

# # 马
horse = PhotoImage(file = "./img/b_j.png")
image = canvas.create_image((start_x + space, start_y), image=horse)

# # 象
elephant = PhotoImage(file = "./img/b_c.png")
image3 = canvas.create_image((start_x + 2 * space, start_y + 2 * space), image=elephant)
 
# 士
guarder = PhotoImage(file = "./img/b_c.png")
image = canvas.create_image((start_x + space, start_y + space), image=guarder)

# test = PhotoImage(file = "./img/b_c.png")
# image = canvas.create_image((5 * start_x + 80, start_y), image=test)

# test1 = PhotoImage(file = "./img/b_c.png")
# image = canvas.create_image((6 * start_x + 100, start_y), image=test1)

# test2 = PhotoImage(file = "./img/b_c.png")
# image = canvas.create_image((7 * start_x + 120, start_y), image=test2)

# test3 = PhotoImage(file = "./img/b_c.png")
# image = canvas.create_image((8 * start_x + 140, start_y), image=test3)

# test4 = PhotoImage(file = "./img/b_c.png")
# image = canvas.create_image((9 * start_x + 160, start_y), image=test4)

# test5 = PhotoImage(file = "./img/b_c.png")
# image = canvas.create_image((start_x, 2 * start_y + 20), image=test5)

# test6 = PhotoImage(file = "./img/b_c.png")
# image = canvas.create_image((start_x, 3 * start_y + 40), image=test6)

# test7 = PhotoImage(file = "./img/b_c.png")
# image = canvas.create_image((start_x, 4 * start_y + 60), image=test7)

# test8 = PhotoImage(file = "./img/b_c.png")
# image = canvas.create_image((start_x, 5 * start_y + 80), image=test8)

# test9 = PhotoImage(file = "./img/b_c.png")
# image = canvas.create_image((start_x, 6 * start_y + 100), image=test9)

# test10 = PhotoImage(file = "./img/b_c.png")
# image = canvas.create_image((start_x, 7 * start_y + 120), image=test10)

# test11 = PhotoImage(file = "./img/b_c.png")
# image = canvas.create_image((start_x, 8 * start_y + 140), image=test11)

# test12 = PhotoImage(file = "./img/b_c.png")
# image12 = canvas.create_image((start_x, 9 * start_y + 160), image=test12)


# test13 = PhotoImage(file = "./img/b_c.png")
# image13 = canvas.create_image((start_x, 10 * start_y + 180), image=test13)

box = PhotoImage(file = "./img/r_box.png")
choice = 0

def test_bind(event):
    global choice
    tag_id = canvas.find_closest(event.x, event.y)
    choice = tag_id
    if not tag_id:
        return
    x, y = canvas.coords(tag_id)
    image13 = canvas.create_image((x+1, y+1), image=box)
    canvas.update()

def luo(event):
    global choice
    i = int((event.x - 4) / space)
    j = int((event.y - 6)/ space)
    new_x, new_y = (start_x + i * space), (start_y + j * space)
    old_x, old_y = canvas.coords(choice)

    import time
    for i in range( int((int(new_x) - int(old_x)) / 10) ):
        time.sleep(0.1)
        canvas.move(choice, 10, 0)
        canvas.update()

# image13 = canvas.create_image((start_x, 10 * start_y + 180), image=test13)

# canvas.bind('<Button-1>', test_bind)

canvas.tag_bind(image3, '<Button-1>', test_bind)
canvas.bind('<Button-1>', luo)


# test14 = PhotoImage(file = "./img/b_c.png")
# image = canvas.create_image((start_x, 11 * start_y + 200), image=test14)



# soldie general cannons
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
