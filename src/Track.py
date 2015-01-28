import pygame
from Sound import Sound
import Color
import DrawText

WIDTH = 600
HEIGHT = 50



class Track:

	sound = None
	is_selected = False

	def __init__(self, sound):
		self.sound = sound

	def get_sound(self):
		return self.sound

	def set_selected(self, val):
		self.is_selected = val

	def get_selected(self):
		return self.is_selected
	
	def draw(self, surface, num=0):
		# num
		num_col = Color.bg_selected_track if self.is_selected else Color.bg_track
		pygame.draw.rect(surface, num_col, (0,0, 20,HEIGHT), 0)
		DrawText.draw(surface, str(num), 5, 25)
		# title
		pygame.draw.rect(surface, Color.darkBlue, (20,0,WIDTH-20,HEIGHT), 0)
		DrawText.draw(surface, self.sound.get_name(), 25, 25)
		# status
		pygame.draw.rect(surface, Color.yellow, (200, 0,WIDTH-200,HEIGHT), 0)
		


