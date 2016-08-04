import pygame
import random

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
AZURE = (240, 255, 255)
AQUAMARINE = (127, 255, 212)
GREY = (129, 129, 129)
CORNFLOWERBLUE = (100, 149, 237)
ORANGERED = (255, 69, 0)
PLUM = (221, 160, 221)
colors = [AZURE, BLACK, GREEN, BLUE, RED, AQUAMARINE, CORNFLOWERBLUE, ORANGERED, PLUM]

def random_color():
    return random.choice(colors)

pygame.init()



# Set the width and height of the screen [width, height]
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# Set the title of the window
pygame.display.set_caption("CityScroller")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()



class Building(object):
    color=random_color()
    """
    This class will be used to create the building objects.

    It takes:
      x_point - an integer that represents where along the x-axis the building will be drawn
      y_point - an integer that represents where along the y-axis the building will be drawn
      Together the x_point and y_point represent the top, left corner of the building

      width - an integer that represents how wide the building will be in pixels.
            #A positive integer draws the building right to left(->).
            #A negative integer draws the building left to right (<-).
      height - an integer that represents how tall the building will be in pixels
            #A positive integer draws the building up 
            #A negative integer draws the building down 
      
      color - a tuple of three elements which represents the color of the building
            #Each element being a number from 0 - 255 that represents how much red, green and blue the color should have.

    It depends on:
        pygame being initialized in the environment.
        It depends on a "screen" global variable that represents the surface where the buildings will be drawn
        

    """
    def __init__(self, x_point, y_point,width, height, color):
       self.x_point = x_point
       self.width = width
       self.height = height
       self.y_point = y_point
       self.color = color
    def draw(self):
        #pygame.draw.rect(surface,color,rect,width)
      pygame.draw.rect(screen,self.color,(self.x_point,self.y_point, self.width,self.height),0)
            
        
    def move(self, speed):
        while not true:
            self.x_point += speed
        """
        Takes in an integer that represents the speed at which the building is moving
            A positive integer moves the building to the right ->
            A negative integer moves the building to the left  <-
        Moves the building horizontally across the screen by changing the position of the
        x_point by the speed
        """

class Scroller(object):
    color=random_color()
    
    buildings=[]

    def __init__(self, width, height, base, color, speed):
            self.width = width  
            self.height = height
            self.base = base
            self.speed = speed
            self.color = color
            self.buildings = buildings
            self.add_buildings()
    def add_buildings(self):
      total_width = 0
      while total_width <= self.width:
            self.add_building(total_width)
            last_index = len(buildings)-1
            total_width = self.buildings[last_index].width
        
                #calls add_building function below
    def add_building(self, x_location):
        #add building to list of buildings.append
        height = random.randint(0, self.height)
        width = random.randint(0, self.width)
        y_point = self.base - height
        new_building = Building(x_location, y_point, width, height, color)
        self.buildings.append(new_building)
        """
        takes in an x_location, an integer, that represents where along the x-axis to
        put a buildng.
        Adds a building to list of buildings.
        """

    def draw_buildings(self):
        for building in self.buildings:
          building.draw()
    def move_buildings(self):
        for building in self.buildings:
            building.move(self.speed)
          
        last_index = len(self.buildings)-1  
        last_building = self.buildings[last_index]
        new_position = last_building.width +last_building.x_point
        
        self.add_building(new_position)
        
        
FRONT_SCROLLER_COLOR = (0,0,30)
MIDDLE_SCROLLER_COLOR = (30,30,100)
BACK_SCROLLER_COLOR = (50,50,150)
BACKGROUND_COLOR = (17, 9, 89)

front_scroller = Scroller(SCREEN_WIDTH, 500, SCREEN_HEIGHT, FRONT_SCROLLER_COLOR, 3)
middle_scroller = Scroller(SCREEN_WIDTH, 200, (SCREEN_HEIGHT - 50), MIDDLE_SCROLLER_COLOR, 2)
back_scroller = Scroller(SCREEN_WIDTH, 20, (SCREEN_HEIGHT - 100), BACK_SCROLLER_COLOR, 1)
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLUE)

    # --- Drawing code should go here

    back_scroller.draw_buildings()
    back_scroller.move_buildings()
    middle_scroller.draw_buildings()
    middle_scroller.move_buildings()
    front_scroller.draw_buildings()
    front_scroller.move_buildings()


    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
exit() # Needed when using IDLE
