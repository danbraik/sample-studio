import pygame
import Color
import DrawText

WIDTH = 600
HEIGHT = 143


class Track:

	def __init__(self, soundpath):
		self._sound = pygame.mixer.Sound(soundpath)
		self._name = soundpath.split("/")[-1]
		self._is_selected = False
		self._nb_playing = 0
		self._img = None
	
	def set_imagepath(self, path):
		self._img = pygame.image.load(path)

	def get_name(self):
		return self._name

	def get_sound(self):
		return self._sound


	def set_selected(self, val):
		self._is_selected = val

	def is_selected(self):
		return self._is_selected

	
	def add_playing(self):
		self._nb_playing += 1

	def sub_playing(self):
		if self._nb_playing == 0:
			raise Error("Track - sub_playing")
		self._nb_playing -= 1

	def is_playing(self):
		return self._nb_playing > 0

	
	def draw(self, surface, num=0):
		w_num = 20
		x_title = w_num + 5
		surface.fill(Color.darkBlue)
		# num
		num_col = Color.bg_selected_track if self.is_selected() else Color.bg_track
		pygame.draw.rect(surface, num_col, (0,0, w_num, HEIGHT), 0)
		DrawText.draw(surface, str(num), 5, HEIGHT/2)
		# visualization
		if self._img:
			surface.blit(self._img, (w_num, 0, WIDTH, 147))
		# title
		# pygame.draw.rect(surface, Color.darkBlue, (20,0,WIDTH-20,HEIGHT), 0)
		DrawText.draw(surface, self.get_name(), x_title, 5)
		# status
		if self.is_playing():
			w_r = 2
			pygame.draw.rect(surface, Color.yellow, (w_num, 0, WIDTH-w_num-1, HEIGHT-1), w_r)



