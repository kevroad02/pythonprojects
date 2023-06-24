import pygame
import time
import random

WIDTH, HEIGHT = 800,600
WIN= pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge")

# Loading background image
BG= pygame.image.load("/storage/emulated/0/Documents/Termux/mainPyFolder/space.png")

def draw():
	# Blit is method for drawing
	WIN.blit(BG, (0,0))
	pygame.display.update()

def main():
	run = True
	
	while run:
		for event in pygame.event.get():
			# If Closed
			if event.type == pygame.QUIT:
				run = False
				break
		draw()
	
	pygame.quit()

# Making sure the file that's being run isn't an imported file	
if __name__ == "__main__":
	main()
