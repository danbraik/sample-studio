import pygame
import Color
import DrawText

WIDTH = 600
HEIGHT = 143


class Track:

	def __init__(self, sound, soundname, image):
		self._sound = sound
		self._name = soundname 
		self._is_selected = False
		self._nb_playing = 0
		self._img = image
		self._time = 0


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
		self._time = pygame.time.get_ticks();

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

		# length
		length = int(self._sound.get_length())
		DrawText.draw(surface, str(length), WIDTH - 60, 5)

		# status
		if self.is_playing():
			w_r = 2
			pygame.draw.rect(surface, Color.yellow, (w_num, 0, WIDTH-w_num-1, HEIGHT-1), w_r)
			
			if self._img:
			    time = pygame.time.get_ticks();
			    x_pos = ((time - self._time) / length * (self._img.get_width())) / 1000.0 + w_num
			    pygame.draw.line(surface, Color.orange, (x_pos, 0), (x_pos, HEIGHT), 2);


