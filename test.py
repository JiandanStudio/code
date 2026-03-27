import turtle
import math

# 设置画布和画笔
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("跳动的心形动画")

heart = turtle.Turtle()
heart.speed(0)  # 最快速度
heart.hideturtle()

# 绘制心形的函数
def draw_heart(size, color):
    heart.color(color)
    heart.begin_fill()
    
    # 使用参数方程绘制心形
    for angle in range(360):
        t = math.radians(angle)
        x = size * 16 * math.sin(t)**3
        y = -size * (13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
        heart.goto(x, y)
    
    heart.end_fill()

# 主动画循环
try:
    while True:
        # 绘制从小到大的心形，颜色渐变
        for i in range(1, 20):
            heart.clear()
            # 颜色从深红到粉红渐变
            r = 255
            g = int(100 + i * 7)
            b = int(100 + i * 7)
            color = (r/255, g/255, b/255)
            draw_heart(i, color)
            screen.update()
            turtle.delay(10)
        
        # 绘制从大到小的心形，颜色渐变
        for i in range(19, 0, -1):
            heart.clear()
            # 颜色从粉红到深红渐变
            r = 255
            g = int(100 + i * 7)
            b = int(100 + i * 7)
            color = (r/255, g/255, b/255)
            draw_heart(i, color)
            screen.update()
            turtle.delay(10)
except KeyboardInterrupt:
    # 按 Ctrl+C 退出程序
    screen.bye()