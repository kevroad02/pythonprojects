import pygame
import time
import random
pygame.font.init()

# Defining variables for window width and height
WIDTH, HEIGHT = 400,300
WIN= pygame.display.set_mode((WIDTH, HEIGHT))
# Sets top screen thingy name / caption
pygame.display.set_caption("Space Dodge")

# Loading background image with scale as 800,600 (does not preserve aspect ratio)
BG= pygame.transform.scale(pygame.image.load("/storage/emulated/0/Documents/Termux/mainPyFolder/space.png"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5

FONT = pygame.font.SysFont("comicsans", 30)

# Must pass player into draw
def draw(player, elapsed_time):
	# Blit is method for drawing
	WIN.blit(BG, (0,0))
	# Draw on window, a red player
	pygame.draw.rect(WIN, "red", player)
	# Refreshes game
	pygame.display.update()
	
	
def main():
	run = True
	
	# X position, Y position, Width, Height
	player = pygame.Rect(200, HEIGHT-PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
	
	# Clock so the game doesn't run at different FPS on different computers and glitches the game out
	clock = pygame.time.Clock()
	
	# Getting time at the start from declaring a variable
	start_time = time.time()
	# Declaring variable here . . .
	elapsed_time = 0
	
	while run:
		clock.tick(60)
		# Every time we iterate we're minusing time from start time to get elapsed time
		elapsed_time = time.time() - start_time
		for event in pygame.event.get():
			# If Game Closed, run = false
			if event.type == pygame.QUIT:
				run = False
				break
		
		# Defines variable for the keys so you don't have to type it out every time
		keys = pygame.key.get_pressed()
		if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
			player.x -= PLAYER_VEL
		if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
			player.x += PLAYER_VEL
		# Passes player into being drawn
		draw(player, elapsed_time)
	
	pygame.quit()

# Making sure the file that's being run isn't an imported file	
if __name__ == "__main__":
	main()
