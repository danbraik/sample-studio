import pygame


class Sound:
	sound = None
	name = ""
	

	def __init__(self, filepath):
		self.sound = pygame.mixer.Sound(filepath)
		self.name = filepath.split("/")[-1]	

	def get_name(self):
		return self.name

	def play(self):
		self.sound.play()

	def fadein(self, time=2000):
		self.sound.play(fade_ms=time)

	def stop(self):
		self.sound.stop()

	
