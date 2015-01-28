import pygame
import Color

FONT = None


def draw(surface, txt, x=0, y=0, color=Color.white):
	global FONT
	if FONT == None:
		FONT = pygame.font.SysFont("monospace", 15)
	label = FONT.render(txt, 0, color)
	surface.blit(label, (x, y))

