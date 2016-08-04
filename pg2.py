import pygame

# initialize all mudules in pygame
pygame.init()

# define colors
BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)
BLUE=(0,0,255)

# set width and height of the screen (x,y)

size=(700,500)
screen=pygame.display.set_mode(size)

#include a caption on screen
pygame.display.set_caption("My Fabulous Game")

#loop until user clicks "close button"
done = False 

#clock is used to manage how fast your screen updates
clock=pygame.time.Clock()

#----- Main Loop -----#
while not done:
	#----Main event loop----#
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			done=True 	
 
		#game logic goes here##
		
		
		#screen- clearing code goes here##
		
		#Here, we clear the screen to white. Don't put the drawing above this, or they will be erased by the command
		
		#If you want a background image,rplace this clear with blit'ing the background image using pygame.blit()
		screen.fill(WHITE)
		
		
		#----- drawing code goes here -----#
		#pygame.draw.rect(surface,color,start,end,width=1)
		#draw red diagonal line
		pygame.draw.rect(screen, RED, (0,0),(700,500),2)
		
		#---- Update the screen with drawing
		pygame.display.flip()
		#pygame.display.update()
		
		# -- limit to 60 frames per second--#
		clock.tick(60)

		
pygame.quit()
exit()
