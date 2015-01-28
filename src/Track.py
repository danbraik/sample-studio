import pygame
import Color
import DrawText

WIDTH = 600
HEIGHT = 50


class Track:

	def __init__(self, soundpath):
		self._sound = pygame.mixer.Sound(soundpath)
		self._name = soundpath.split("/")[-1]
		self._is_selected = False
		self._is_playing = False

	def get_name(self):
		return self._name

	def get_sound(self):
		return self._sound


	def set_selected(self, val):
		self._is_selected = val

	def is_selected(self):
		return self._is_selected

	
	def set_playing(self, val):
		self._is_playing = val

	def is_playing(self):
		return self._is_playing

	
	def draw(self, surface, num=0):
		# num
		num_col = Color.bg_selected_track if self.is_selected() else Color.bg_track
		pygame.draw.rect(surface, num_col, (0,0, 20,HEIGHT), 0)
		DrawText.draw(surface, str(num), 5, 25)
		# title
		pygame.draw.rect(surface, Color.darkBlue, (20,0,WIDTH-20,HEIGHT), 0)
		DrawText.draw(surface, self.get_name(), 25, 25)
		# status
		stat_col = Color.yellow if self.is_playing() else Color.bg_track
		pygame.draw.rect(surface, stat_col, (200, 0,WIDTH-200,HEIGHT), 0)


