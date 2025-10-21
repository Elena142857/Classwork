import pygame    # 导入pygame

# Initialize Pygame    (初始化 Pygame)
pygame.init()    # 激活 Pygame 的所有子模块（如显示模块、字体模块、声音模块、事件处理模块等）

# Set the screen size  (设置屏幕尺寸)（新增说明）
WIDTH = 640    # 定义窗口的宽度（单位：像素）
HEIGHT = 480    # 定义窗口的高度（单位：像素）
SIZE = (WIDTH, HEIGHT)    # 将宽度和高度组合成 Pygame 要求的 “窗口尺寸元组”
screen = pygame.display.set_mode(SIZE)     # 初始化一个显示窗口
pygame.display.set_caption("Landscape Lab")    # (新增）设置图像名称“景观实验室”
clock = pygame.time.Clock()    # 创建一个控制游戏帧率的时钟对象，控制游戏帧率（FPS）

# ---------------------------
# Initialize global variables    初始化全局变量
# ---------------------------

# [修改开始_新增云朵移动]
# Cloud position variables and velocity variables  云朵位置变量和速度变量 
cloud_x = 100  # 云朵初始x位置
cloud_speed = 1.5  # 云朵移动速度
# [修改结束]

# [修改开始：新增太阳移动]
# Sun position and speed variables  太阳位置和速度变量 
sun_x = -50  # 太阳初始x位置（从屏幕左侧外开始）
sun_speed = 2  # 太阳移动速度
sun_radius = 40  # 太阳半径
sun_color = (255, 255, 0)  # 黄色太阳
# [修改结束]

# [修改开始：新增月亮移动]
# Moon position and speed variables  月亮位置和速度变量
moon_x = -50  # 月亮初始x位置
moon_speed = 2  # 月亮移动速度
moon_radius = 40  # 月亮半径
moon_color = (220, 220, 220)  # 浅灰色月亮
# [修改结束]

# [修改开始：昼夜颜色]
# Day-night state and color variables  昼夜状态和颜色变量 
day_mode = True  # 初始为白天模式
day_sky_color = (135, 206, 235)  # 白天天空颜色（天蓝色）
night_sky_color = (0, 0, 50)  # 夜晚天空颜色（深蓝色）
# [修改结束]

# [修改开始：山和房子颜色]
# Mountain and house color variables  山和房子颜色变量 
mountain_color = (70, 70, 70)  # 山脉颜色
house_color = (139, 69, 19)  # 房子颜色（棕色）
roof_color = (100, 50, 0)  # 屋顶颜色（深棕色）
window_color = (255, 255, 150)  # 窗户颜色（浅黄色）
# [修改开始：结束]

running = True    # 游戏主循环，当 Running = False时退出循环，循环频率由 clock.tick(FPS)控制（通常60FPS）
while running:
    # EVENT HANDLING  事件处理
    for event in pygame.event.get():    # 事件处理系统，pygame.event.get()获取当前帧的所有待处理事件
        if event.type == pygame.QUIT:    # 退出事件处理
            running = False    
        elif event.type == pygame.MOUSEBUTTONDOWN:
            print(event.pos)

    # GAME STATE UPDATES  游戏状态更新
    # [修改开始：云朵移动]
    # Cloud position update logic  云朵位置更新逻辑 
    cloud_x += cloud_speed  # 云朵水平移动速度为1.5（cloud_speed定义见21行）
    if cloud_x > WIDTH + 200:  # 当云朵完全移出屏幕右侧
        cloud_x = -200  # 重置到屏幕左侧
    # [修改结束]

    # [修改开始：太阳移动及昼夜颜色切换]
    # Logic for updating the sun's position and switching between day and night  太阳位置更新和昼夜切换逻辑
    if day_mode:  # 只在白天更新太阳位置
        sun_x += sun_speed  # 太阳水平移动速度为2（sun_speed定义见27行）
        if sun_x > WIDTH + sun_radius:  # 判断条件：太阳移出屏幕右侧
            day_mode = False  # 切换到夜晚
            moon_x = -moon_radius  # 重置月亮位置
    # [修改结束]

    # [修改开始：月亮移动及昼夜颜色切换]
    # Logic for updating the moon's position and switching between day and night  月亮位置更新和昼夜切换逻辑
    if not day_mode:  # 只在夜晚更新月亮位置
        moon_x += moon_speed  # 月亮水平移动速度为2（moon_speed定义见35行）
        if moon_x > WIDTH + moon_radius:  # 月亮移出屏幕右侧
            day_mode = True  # 切换到白天
            sun_x = -sun_radius  # 重置太阳位置
    # [修改结束]

    # DRAWING  绘画
    # [修改开始：天空颜色切]
    # Sky background color switching logic  天空背景颜色切换逻辑
    current_sky_color = day_sky_color if day_mode else night_sky_color
    screen.fill(current_sky_color)    # 计算并设置当前天空颜色
    # [修改结束]

    # [修改开始：太阳绘制]
    # Sun drawing logic  太阳绘制逻辑
    if day_mode:  # 只在白天显示太阳
        pygame.draw.circle(screen, sun_color, (int(sun_x), 100), sun_radius)
    # [修改结束]

    # 
    # [修改开始：月亮绘制]
    # Moon drawing logic  月亮绘制逻辑 
    if not day_mode:  # 只在夜晚显示月亮
        pygame.draw.circle(screen, moon_color, (int(moon_x), 100), moon_radius)
    # [修改结束]

    # [修改开始：云朵绘制]
    # Cloud drawing logic  云朵绘制逻辑
    radius = 30  # 定义组成云朵的每个圆形的半径为 30 像素。统一尺寸确保云朵形态协调。
    cloud_color = (220, 220, 220) if day_mode else (100, 100, 100)  # 云朵昼夜颜色变化
    pygame.draw.circle(screen, cloud_color, (cloud_x + 14, 188), radius)
    pygame.draw.circle(screen, cloud_color, (cloud_x + 54, 155), radius)
    pygame.draw.circle(screen, cloud_color, (cloud_x + 54, 190), radius)
    pygame.draw.circle(screen, cloud_color, (cloud_x + 85, 177), radius)
    # [修改结束]

    # [修改开始：绘制山脉]
    # Draw a big mountain  绘制大山
    pygame.draw.polygon(screen, mountain_color, [
        (WIDTH-400, HEIGHT),  # 山脚右
        (WIDTH-200, HEIGHT-250),  # 山顶
        (WIDTH, HEIGHT)  # 山脚左
    ])
    # Draw a small mountain  绘制小山
    pygame.draw.polygon(screen, mountain_color, [
        (WIDTH-600, HEIGHT),  # 山脚右
        (WIDTH-450, HEIGHT-150),  # 山顶
        (WIDTH-300, HEIGHT)  # 山脚左
    ])
    # [修改结束]

    # [修改开始：绘制房子]
    # The house is located at the foot of the mountain.  房子位置在山脚下
    house_x, house_y = WIDTH-350, HEIGHT-100  # Location of the house  房子位置
    pygame.draw.rect(screen, house_color, (house_x, house_y, 100, 80))  # Main body of the house  房子主体
    # roof  屋顶
    pygame.draw.polygon(screen, roof_color, [
        (house_x, house_y), 
        (house_x+50, house_y-50), 
        (house_x+100, house_y)
    ])
    pygame.draw.rect(screen, (70, 35, 0), (house_x+40, house_y+30, 30, 50))    # door  门
    # 窗户
    pygame.draw.rect(screen, window_color, (house_x+15, house_y+15, 25, 25))    # window1  窗户1
    pygame.draw.rect(screen, window_color, (house_x+65, house_y+15, 25, 25))    # window2  窗户2
    # [修改结束]

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
