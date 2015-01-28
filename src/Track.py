import pygame
from Sound import Sound
import Color
import DrawText

WIDTH = 200
HEIGHT = 50



class Track:

	sound = None

	def __init__(self, sound):
		self.sound = sound

	def get_sound(self):
		return self.sound
	
	def draw(self, surface):
		pygame.draw.rect(surface, Color.darkBlue, (0,0,WIDTH,HEIGHT), 0)
		DrawText.draw(surface, self.sound.get_name(), 10, 25)


