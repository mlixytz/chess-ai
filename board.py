from tkinter import Tk, Canvas, PhotoImage, mainloop, Button, Label
from common import *

WIDTH, HEIGHT = 530, 580
start_x, start_y = 37, 39
space = 57
choice = 0
box_tag = 0

tk = Tk()
canvas = Canvas(tk, width=WIDTH, height=HEIGHT)

# 存储棋盘与棋子信息
board = []

# 存储棋盘与canvas tag信息
board_tag = []

photo_image_dict = {}


def index2xy(index):
    """ 获取一维数组索引在棋盘上对应的x、y坐标，如果不在棋盘返回 None """
    start_row = start_col = 3
    end_row, end_col = 12, 11
    y, x = divmod(index, 16)
    if x < start_row or x > end_row or y < start_col or y > end_col:
        return
    return x - 3, y - 3

def xy2index(x, y):
    """ 棋盘上的x、y坐标在一维数组中对应的索引 """
    return (y + 3) * 16 + x + 3

def xy2pixel(x, y):
    """ 获取棋盘中 x, y 坐标对应的像素 """
    return start_x + x * space, start_y + y * space

def pixel2xy(px, py):
    """ 根据像素定位棋盘的x、y坐标 """
    x = int((px - 4) / space)
    y = int((py - 6)/ space)
    return x, y


def create_image(img_str):
    """ 在canvas上创建图片, 返回photoImage对象"""
    if img_str in photo_image_dict:
        img = photo_image_dict[img_str]
    else:
        img = PhotoImage(file=IMG_PATH + img_str)
        photo_image_dict[img_str] = img
    return img


def create_piece(x, y, img_str):
    """ 创建棋子

        传入棋盘位置x，y，和要创建的棋子图片
    """
    img = create_image(img_str)
    tag = canvas.create_image(*xy2pixel(x, y), image=img)
    board[xy2index(x, y)] = PIECES_NUM[img_str]
    board_tag[xy2index(x, y)] = tag

    return tag


def bg_init():
    """ 棋盘初始化 """
    img = create_image(BG)
    canvas.create_image((WIDTH/2, HEIGHT/2), image=img)


def piece_init():
	""" 棋子初始化 """

	# 红车
	create_piece(0, 0, RED_VEHICLE)
	create_piece(8, 0, RED_VEHICLE)

    # 红马
	create_piece(1, 0, RED_HORSE)
	create_piece(7, 0, RED_HORSE)

    # 红相
	create_piece(2, 0, RED_ELEPHANT)
	create_piece(6, 0, RED_ELEPHANT)

    # 红仕
	create_piece(3, 0, RED_GUARDER)
	create_piece(5, 0, RED_GUARDER)

    # 红帅
	create_piece(4, 0, RED_GENERAL)

    # 红炮
	create_piece(1, 2, RED_CANNON)
	create_piece(7, 2, RED_CANNON)

    # 红兵
	create_piece(0, 3, RED_SOLDIE)
	create_piece(2, 3, RED_SOLDIE)
	create_piece(4, 3, RED_SOLDIE)
	create_piece(6, 3, RED_SOLDIE)
	create_piece(8, 3, RED_SOLDIE)

    # 黑车
	create_piece(0, 9, BLACK_VEHICLE)
	create_piece(8, 9, BLACK_VEHICLE)

    # 黑马
	create_piece(1, 9, BLACK_HORSE)
	create_piece(7, 9, BLACK_HORSE)

    # 黑象
	create_piece(2, 9, BLACK_ELEPHANT)
	create_piece(6, 9, BLACK_ELEPHANT)

    # 黑士
	create_piece(3, 9, BLACK_GUARDER)
	create_piece(5, 9, BLACK_GUARDER)

    # 黑将
	create_piece(4, 9, BLACK_GENERAL)

	# 黑炮
	create_piece(1, 7, BLACK_CANNON)
	create_piece(7, 7, BLACK_CANNON)

    # 黑卒
	create_piece(0, 6, BLACK_SOLDIE)
	create_piece(2, 6, BLACK_SOLDIE)
	create_piece(4, 6, BLACK_SOLDIE)
	create_piece(6, 6, BLACK_SOLDIE)
	create_piece(8, 6, BLACK_SOLDIE)


def board_init():
    """ 棋盘初始化

        棋盘使用一维数组表示，大小为256，也就是 16 X 16 个格子，索引表示棋盘位置，
        值为0表示没有棋子，8~14依次表示红方的帅、仕、相、马、车、炮和兵，16~22依次
        表示黑方的将、士、象、马、车、炮和卒。
    """
   
    for _ in range(256):
        board.append(0)
        board_tag.append(0)

    bg_init()
    piece_init()


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


def move(old_index, event):
    """ 落子 """
    global choice, box_tag
    x, y = pixel2xy(event.x, event.y)
    index = xy2index(x, y)
    tag = board_tag[index]
    if not tag:
        canvas.delete(tag)
        board[index] = create_piece(x, y, NUM_PIECES[board[old_index]])
        board_tag[index] = board[old_index]
        board[old_index] = 0
        board_tag[old_index] = 0
    

def hit(event):
    """ 选择棋子 """
    global choice, box_tag
    x, y = pixel2xy(event.x, event.y)
    index = xy2index(x, y)
    tag = board_tag[index]
    if not tag:
        return
    choice = tag
    px, py = xy2pixel(x, y)
    
    if box_tag:
        canvas.delete(box_tag)

    box = create_image(BOX)
    box_tag = canvas.create_image((px+1, py+1), image=box)
    canvas.update()


canvas.bind('<Button-1>', hit)

board_init()
canvas.pack()
tk.mainloop()
