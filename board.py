from tkinter import Tk, Canvas, PhotoImage, mainloop, Button, Label
from common import *

WIDTH, HEIGHT = 530, 580
start_x, start_y = 37, 39
space = 57

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)


board = []
pixel_board = []

photo_image_dict = {}


def index2xy(index):
    """ 获取一维数组索引在棋盘上对应的x、y坐标，如果不在棋盘返回 None """
    start_row = start_col = 3
    end_row, end_col = 12, 11
    if x < start_row or x > end_row or y < start_col or y > end_col:
        return
    x, y = divmod(index, 16)
    return x - 3, y - 3

def xy2index(x, y):
    """ 棋盘上的x、y坐标在一维数组中对应的索引 """
    return (x + 3) * 16 + y + 3

def xy2pixel(x, y):
    """ 获取棋盘中 x, y 坐标对应的像素 """
    return start_x + x * space, start_y + y * space

def pixel2xy(px, py):
    """ 根据像素定位棋盘的x、y坐标 """
    x = int((px - 4) / space)
    y = int((py - 6)/ space)
    return x, y

def create_piece(x, y, img_str):
    """ 创建棋子

        传入棋盘位置x，y，和要创建的棋子图片
    """
    if img_str in photo_image_dict:
        img = photo_image_dict[img_str]
    else:
        img = PhotoImage(file=IMG_PATH + img_str)
        photo_image_dict[img_str] = img

    canvas.create_image(*xy2pixel(x, y), image=img)
    board[xy2index(x, y)] = PIECES_NUM[img_str]

def bg_init():
    """ 棋盘初始化 """
    bg = PhotoImage(file=IMG_PATH + BG)
    canvas.create_image((WIDTH/2, HEIGHT/2), image=bg)

def piece_init():
	""" 棋子初始化 """

	# 红车
	create_piece(0, 0, RED_VEHICLE)
	create_piece(0, 8, RED_VEHICLE)

    # 红马
	create_piece(0, 1, RED_HORSE)
	create_piece(0, 7, RED_HORSE)

    # 红相
	create_piece(0, 2, RED_ELEPHANT)
	create_piece(0, 6, RED_ELEPHANT)

    # 红仕
	create_piece(0, 3, RED_GUARDER)
	create_piece(0, 5, RED_GUARDER)

    # 红帅
	create_piece(0, 4, RED_GENERAL)

    # 红兵
	create_piece(3, 0, RED_SOLDIE)
	create_piece(3, 2, RED_SOLDIE)
	create_piece(3, 4, RED_SOLDIE)
	create_piece(3, 6, RED_SOLDIE)
	create_piece(3, 8, RED_SOLDIE)

    # 黑车
	create_piece(9, 0, BLACK_VEHICLE)
	create_piece(9, 8, BLACK_VEHICLE)

    # 黑马
	create_piece(9, 1, BLACK_HORSE)
	create_piece(9, 7, BLACK_HORSE)

    # 黑象
	create_piece(9, 2, BLACK_ELEPHANT)
	create_piece(9, 6, BLACK_ELEPHANT)

    # 黑士
	create_piece(9, 3, BLACK_GUARDER)
	create_piece(9, 5, BLACK_GUARDER)

    # 黑将
	create_piece(9, 4, BLACK_GENERAL)

    # 黑卒
	create_piece(6, 0, BLACK_SOLDIE)
	create_piece(6, 2, BLACK_SOLDIE)
	create_piece(6, 4, BLACK_SOLDIE)
	create_piece(6, 6, BLACK_SOLDIE)
	create_piece(6, 8, BLACK_SOLDIE)


def board_init():
    """ 棋盘初始化

        棋盘使用一维数组表示，大小为256，也就是 16 X 16 个格子，索引表示棋盘位置，
        值为0表示没有棋子，8~14依次表示红方的帅、仕、相、马、车、炮和兵，16~22依次
        表示黑方的将、士、象、马、车、炮和卒。
    """
   
    for i in range(256):
        board.append(0)

    bg_init()
    piece_init()


board_init()
canvas.pack()
tk.mainloop()


# # 棋盘
# img = PhotoImage(file='./img/bg.png')
# canvas.create_image((WIDTH/2, HEIGHT/2), image=img, state='normal')

# # 棋子
# # 车
# vehicle = PhotoImage(file = "./img/b_j.png")
# image1 = canvas.create_image((start_x, start_y), image=vehicle)

# # # 马
# horse = PhotoImage(file = "./img/b_j.png")
# image = canvas.create_image((start_x + space, start_y), image=horse)

# # # 象
# elephant = PhotoImage(file = "./img/b_c.png")
# image3 = canvas.create_image((start_x + 2 * space, start_y + 2 * space), image=elephant)
 
# # 士
# guarder = PhotoImage(file = "./img/b_c.png")
# image = canvas.create_image((start_x + space, start_y + space), image=guarder)

# # test = PhotoImage(file = "./img/b_c.png")
# # image = canvas.create_image((5 * start_x + 80, start_y), image=test)

# # test1 = PhotoImage(file = "./img/b_c.png")
# # image = canvas.create_image((6 * start_x + 100, start_y), image=test1)

# # test2 = PhotoImage(file = "./img/b_c.png")
# # image = canvas.create_image((7 * start_x + 120, start_y), image=test2)

# # test3 = PhotoImage(file = "./img/b_c.png")
# # image = canvas.create_image((8 * start_x + 140, start_y), image=test3)

# # test4 = PhotoImage(file = "./img/b_c.png")
# # image = canvas.create_image((9 * start_x + 160, start_y), image=test4)

# # test5 = PhotoImage(file = "./img/b_c.png")
# # image = canvas.create_image((start_x, 2 * start_y + 20), image=test5)

# # test6 = PhotoImage(file = "./img/b_c.png")
# # image = canvas.create_image((start_x, 3 * start_y + 40), image=test6)

# # test7 = PhotoImage(file = "./img/b_c.png")
# # image = canvas.create_image((start_x, 4 * start_y + 60), image=test7)

# # test8 = PhotoImage(file = "./img/b_c.png")
# # image = canvas.create_image((start_x, 5 * start_y + 80), image=test8)

# # test9 = PhotoImage(file = "./img/b_c.png")
# # image = canvas.create_image((start_x, 6 * start_y + 100), image=test9)

# # test10 = PhotoImage(file = "./img/b_c.png")
# # image = canvas.create_image((start_x, 7 * start_y + 120), image=test10)

# # test11 = PhotoImage(file = "./img/b_c.png")
# # image = canvas.create_image((start_x, 8 * start_y + 140), image=test11)

# # test12 = PhotoImage(file = "./img/b_c.png")
# # image12 = canvas.create_image((start_x, 9 * start_y + 160), image=test12)


# # test13 = PhotoImage(file = "./img/b_c.png")
# # image13 = canvas.create_image((start_x, 10 * start_y + 180), image=test13)

# box = PhotoImage(file = "./img/r_box.png")
# choice = 0

# def test_bind(event):
#     global choice
#     tag_id = canvas.find_closest(event.x, event.y)
#     choice = tag_id
#     if not tag_id:
#         return
#     x, y = canvas.coords(tag_id)
#     image13 = canvas.create_image((x+1, y+1), image=box)
#     canvas.update()

# def luo(event):
#     global choice
#     i = int((event.x - 4) / space)
#     j = int((event.y - 6)/ space)
#     new_x, new_y = (start_x + i * space), (start_y + j * space)
#     old_x, old_y = canvas.coords(choice)

#     import time
#     for i in range( int((int(new_x) - int(old_x)) / 10) ):
#         time.sleep(0.1)
#         canvas.move(choice, 10, 0)
#         canvas.update()

# # image13 = canvas.create_image((start_x, 10 * start_y + 180), image=test13)

# # canvas.bind('<Button-1>', test_bind)

# canvas.tag_bind(image3, '<Button-1>', test_bind)
# canvas.bind('<Button-1>', luo)


# # test14 = PhotoImage(file = "./img/b_c.png")
# # image = canvas.create_image((start_x, 11 * start_y + 200), image=test14)



# # soldie general cannons
# # vehicle = PhotoImage(file = "./img/b_c.png")
# # image = canvas.create_image((37, 37), image=vehicle)

# # vehicle = PhotoImage(file = "./img/b_c.png")
# # image = canvas.create_image((37, 37), image=vehicle)

# # vehicle = PhotoImage(file = "./img/b_c.png")
# # image = canvas.create_image((37, 37), image=vehicle)

# # vehicle = PhotoImage(file = "./img/b_c.png")
# # image = canvas.create_image((37, 37), image=vehicle)


# # vehicle = PhotoImage(file = "./img/b_c.png")
# # image = canvas.create_image((37, 37), image=vehicle)

# # vehicle = PhotoImage(file = "./img/b_c.png")
# # image = canvas.create_image((37, 37), image=vehicle)


# # vehicle = PhotoImage(file = "./img/b_c.png")
# # image = canvas.create_image((37, 37), image=vehicle)


# # vehicle = PhotoImage(file = "./img/b_c.png")
# # image = canvas.create_image((37, 37), image=vehicle)

# # vehicle = PhotoImage(file = "./img/b_c.png")
# # image = canvas.create_image((37, 37), image=vehicle)


# tk.mainloop()
