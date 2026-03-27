import turtle

# 设置画布和画笔
screen = turtle.Screen()
screen.bgcolor("white")
heart = turtle.Turtle()
heart.color("red")

# 绘制爱心的函数
def draw_heart():
    for i in range(200):
        heart.forward(i)
        heart.left(144)

# 开始绘制
draw_heart()

# 结束绘制并显示结果
turtle.done()