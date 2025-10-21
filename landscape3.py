# pygame template    pygame 模板

import pygame    # 导入pygame

# Initialize Pygame (初始化 Pygame) 
pygame.init()    # 激活 Pygame 的所有子模块（如显示模块、字体模块、声音模块、事件处理模块等）

# Set the screen size (设置屏幕尺寸)（新增说明）
WIDTH = 640    # 定义窗口的宽度（单位：像素）
HEIGHT = 480    # 定义窗口的高度（单位：像素）
SIZE = (WIDTH, HEIGHT)    # 将宽度和高度组合成 Pygame 要求的 “窗口尺寸元组”
screen = pygame.display.set_mode(SIZE)    # 初始化一个显示窗口
pygame.display.set_caption("Landscape Lab")  # (新增）设置图像名称“景观实验室”
clock = pygame.time.Clock()    # 创建一个控制游戏帧率的时钟对象，控制游戏帧率（FPS）

# ---------------------------
# Initialize global variables  初始化全局变量
# ---------------------------

running = True    # 游戏主循环，当 Running = False时退出循环，循环频率由 clock.tick(FPS)控制（通常60FPS）
while running:
    # EVENT HANDLING  事件处理
    for event in pygame.event.get():    # 事件处理系统，pygame.event.get()获取当前帧的所有待处理事件
        if event.type == pygame.QUIT:    # 退出事件处理
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

    # GAME STATE UPDATES  游戏状态更
    # All game math and comparisons happen here  所有游戏的运算和比较都在这里进行

    # DRAWING  绘画
    screen.fill("#87CEEB")  # always the first drawing command

    # Cloud  云
    radius = 30
    pygame.draw.circle(screen, "#ececec", (184, 138), radius)
    pygame.draw.circle(screen, "#ececec", (224, 105), radius)
    pygame.draw.circle(screen, "#ececec", (224, 140), radius)
    pygame.draw.circle(screen, "#ececec", (255, 127), radius)

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)
    #---------------------------


pygame.quit()
