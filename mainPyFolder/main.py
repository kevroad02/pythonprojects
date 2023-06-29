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

STAR_WIDTH = 5
STAR_HEIGHT = 10
STAR_VEL = 5

FONT = pygame.font.SysFont("comicsans", 30)

# Must pass player into draw
def draw(player, elapsed_time, stars):
	# Blit is method for drawing
	WIN.blit(BG, (0,0))
	
	time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
	# Draw time_text blit at 10,10 position
	WIN.blit(time_text, (10,10))
	# Draw on window, a red player
	pygame.draw.rect(WIN, "red", player)
	
	for star in stars:
		pygame.draw.rect(WIN, "white", star)
		
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
	
	
	# 2000 milliseconds star_count+1
	star_add_increment = 2000
	star_count = 0
	stars = []
	hit = False
	
	while run:
		star_count += clock.tick(60)
		# Every time we iterate we're minusing time from start time to get elapsed time
		elapsed_time = time.time() - start_time
		
		if star_count > star_add_increment:
			# Placeholder when iteration amount doesn't matter.
			for _ in range (3):
				star_x = random.randint(0, WIDTH - STAR_WIDTH)
				star = pygame.Rect(star_x, -STAR_HEIGHT, STAR_WIDTH, STAR_HEIGHT)
				stars.append(star)
		
		# Minimum 200, every 50 milliseconds new star, faster and faster(?)
		star_add_increment = max(200, star_add_increment - 50)
		star_count = 0
				
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
		draw(player, elapsed_time, stars)
		
		# stars[:] = copy
		for star in stars[:]:
			star.y += STAR_VEL 
			if star.y > HEIGHT:
					stars.remove(star)
			# if star not equal height check if it's same height as player, INCLUDE HEIGHT
			elif star.y + star.height >= player.y and star.colliderect(player):
			# Collide rect function is from pygame
				stars.remove(star)
				hit = True
				break
			
	pygame.quit()

# Making sure the file that's being run isn't an imported file	
if __name__ == "__main__":
	main()
