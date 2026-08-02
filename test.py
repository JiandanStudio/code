import turtle
import math
import time
import time

# 设置画布和画笔
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("跳动的心形动画")

# 允许使用RGB颜色
screen.colormode(255)

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

# 动画状态
current_size = 1
direction = 1

# 主动画函数
def animate():
    global current_size, direction
    
    heart.clear()
    # 颜色从深红到粉红渐变
    r = 255
    g = int(100 + current_size * 7)
    b = int(100 + current_size * 7)
    color = (r, g, b)
    draw_heart(current_size, color)
    screen.update()
    
    # 更新大小和方向
    current_size += direction
    if current_size >= 19:
        direction = -1
    elif current_size <= 1:
        direction = 1
    
    # 控制动画速度
    time.sleep(0.05)
    
    # 继续下一次动画（非阻塞方式）
    screen.ontimer(animate, 10)

# 启动动画
if __name__ == "__main__":
    try:
        screen.tracer(0)  # 关闭自动刷新
        animate()
        screen.mainloop()
    except KeyboardInterrupt:
        # 按 Ctrl+C 退出程序
        screen.bye()