# Landscape Lab

import pygame    

# Initialize Pygame    
pygame.init()    # Activate all submodules of Pygame

# Set the screen size  
WIDTH = 640    
HEIGHT = 480    
SIZE = (WIDTH, HEIGHT)    
screen = pygame.display.set_mode(SIZE)     # Initialize a display window
pygame.display.set_caption("Landscape Lab")    # Set the image name as "Landscape Laboratory"
clock = pygame.time.Clock()    # Create a clock object that controls the game's frame rate

# ---------------------------
# Initialize global variables    
# ---------------------------

# Cloud position variables and velocity variables   
cloud_x = 100  # Initial x position of the cloud
cloud_speed = 1.5  # Cloud movement speed

# Sun position and speed variables  
sun_x = -50  # Initial x-position of the sun (starting from outside the left side of the screen)
sun_speed = 2  # The speed of the sun's movement
sun_radius = 40  # Solar radius
sun_color = (255, 255, 0)  # Set the color of the sun to yellow

# Moon position and speed variables
moon_x = -50  
moon_speed = 2  
moon_radius = 40  
moon_color = (220, 220, 220)  # Set the color of the moon to light gray

# Day-night state and color variables  
day_mode = True  # Set the initial mode to daytime mode
day_sky_color = (135, 206, 235)  # Set the color of the daytime sky to sky blue
night_sky_color = (0, 0, 50)  # Set the color of the night sky to dark blue

# Mountain and house color variables
mountain_color = (70, 70, 70)  # Set the color of the mountains to dark gray
house_color = (139, 69, 19)  # Set the color of the house to brown
roof_color = (100, 50, 0)  # Set the roof color to dark brown
window_color = (255, 255, 150)  # Set the window color to light yellow

running = True 
while running:    # Game main loop, exit the loop when Running = False
    for event in pygame.event.get():    # pygame.event.get() is used to obtain all current pending "events"
        if event.type == pygame.QUIT:    # pygame.QUIT is Pygame's built-in "window closing event"
            running = False    
        elif event.type == pygame.MOUSEBUTTONDOWN:    # pygame.MOUSEBUTTONDOWN is the "mouse button down event" 
            print(event.pos)

    # GAME STATE UPDATES  
    
    # Cloud position update logic   
    cloud_x += cloud_speed  # Horizontal moving speed of clouds
    if cloud_x > WIDTH + 200:  # Determine whether the cloud has completely moved out of the right side of the screen
        cloud_x = -200  # Reset the cloud to the left side of the screen

    # Logic for updating the sun's position and switching between day and night  
    if day_mode:  # Update the sun's position only during the day
        sun_x += sun_speed  # Horizontal movement speed of the sun
        if sun_x > WIDTH + sun_radius:  # Determine that the sun moves out of the right side of the screen
            day_mode = False  # Switch to night
            moon_x = -moon_radius  # Reset the moon's position

    # Logic for updating the moon's position and switching between day and night
    if not day_mode:  # Only update the moon's position at night
        moon_x += moon_speed  # The horizontal moving speed of the moon
        if moon_x > WIDTH + moon_radius:  # Determine that the moon moves out of the right side of the screen
            day_mode = True  # Switch to daytime
            sun_x = -sun_radius  # Reset the sun's position

    # DRAWING  

    # Sky background color switching logic  
    current_sky_color = day_sky_color if day_mode else night_sky_color
    screen.fill(current_sky_color)    # Calculate and set the current sky color

    # Sun drawing logic  
    if day_mode:  # Only display the sun during the day
        pygame.draw.circle(screen, sun_color, (int(sun_x), 100), sun_radius)

    # Moon drawing logic   
    if not day_mode:  # Only display the moon at night
        pygame.draw.circle(screen, moon_color, (int(moon_x), 100), moon_radius)

    # Cloud drawing logic 
    radius = 30  # Define the radius of each circle that makes up the cloud as 30 pixels.
    cloud_color = (220, 220, 220) if day_mode else (100, 100, 100)  # The color change of clouds day and night
    pygame.draw.circle(screen, cloud_color, (cloud_x + 14, 188), radius)
    pygame.draw.circle(screen, cloud_color, (cloud_x + 54, 155), radius)
    pygame.draw.circle(screen, cloud_color, (cloud_x + 54, 190), radius)
    pygame.draw.circle(screen, cloud_color, (cloud_x + 85, 177), radius)

    # Draw a big mountain  
    pygame.draw.polygon(screen, mountain_color, [
        (WIDTH-400, HEIGHT),  # Set the position of the mountain's right foot
        (WIDTH-200, HEIGHT-250),  # Set the coordinate position of the mountain top
        (WIDTH, HEIGHT)  # Set the position of the mountain's left foot
    ])
    # Draw a small mountain  
    pygame.draw.polygon(screen, mountain_color, [
        (WIDTH-600, HEIGHT),  
        (WIDTH-450, HEIGHT-150),  
        (WIDTH-300, HEIGHT)  
    ])

    # The house is located at the foot of the mountain. 
    house_x, house_y = WIDTH-350, HEIGHT-100  # Location of the house  
    pygame.draw.rect(screen, house_color, (house_x, house_y, 100, 80))  # Main body of the house
    # roof  
    pygame.draw.polygon(screen, roof_color, [
        (house_x, house_y), 
        (house_x+50, house_y-50), 
        (house_x+100, house_y)
    ])
    pygame.draw.rect(screen, (70, 35, 0), (house_x+40, house_y+30, 30, 50))    # door 
    pygame.draw.rect(screen, window_color, (house_x+15, house_y+15, 25, 25))    # window1
    pygame.draw.rect(screen, window_color, (house_x+65, house_y+15, 25, 25))    # window2

    # Must be the last two lines
    # of the game loop
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
