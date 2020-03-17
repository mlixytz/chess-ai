# 绘制象棋棋盘
import turtle
t = turtle.Pen()
t.width(2)      # 设置画笔粗细
t.speed(10)      # 设置画笔移动速度

# 画竖线
t.penup()
t.goto(-400, -400)
for i in range(9):
    t.pendown()
    if i != 0 and i != 8:
        t.goto(-400+i*100, 0)
        t.penup()
        t.goto(-400+i*100, 100)
        t.pendown()
    t.goto(-400+i*100, 500)
    t.penup()
    t.goto(-400+i*100+100, -400)

# 画横线
t.penup()
t.goto(-400, -400)
for i in range(10):
    t.pendown()
    t.goto(400, -400+i*100)
    t.penup()
    t.goto(-400, -400+i*100+100)

# 画斜线(下面的中心斜线)
t.penup()
t.goto(-100, -400)
t.pendown()
t.goto(100, -200)

t.penup()
t.goto(100, -400)
t.pendown()
t.goto(-100, -200)

# 画斜线（上面的中心斜线）
t.penup()
t.goto(-100, 500)
t.pendown()
t.goto(100, 300)

t.penup()
t.goto(100, 500)
t.pendown()
t.goto(-100, 300)

# 书写楚河汉界
t.penup()
t.goto(-200, 20)
t.write("楚河", align="center", font=("Arial", 30, "normal"))
t.penup()
t.goto(200, 20)
t.write("汉界", align="center", font=("Arial", 30, "normal"))
# 使界面暂停
turtle.done()