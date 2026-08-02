import turtle
import math

# 设置画布和画笔
t = turtle.Turtle()
t.speed(10)  # 绘制速度（0最快，1-10逐渐变快）
turtle.bgcolor("black")  # 背景色
t.color("red", "pink")   # 线条颜色和填充颜色

# 开始填充
t.begin_fill()

# 绘制爱心（使用参数方程）
for i in range(360):
    # 爱心参数方程
    angle = math.radians(i)
    x = 16 * math.sin(angle) ** 3
    y = 13 * math.cos(angle) - 5 * math.cos(2*angle) - 2 * math.cos(3*angle) - math.cos(4*angle)
    
    # 放大图形并移动到中心
    t.goto(x*10, y*10)

# 结束填充
t.end_fill()

# 隐藏画笔
t.hideturtle()

# 保持窗口打开
turtle.done()