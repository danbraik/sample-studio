import pygame
import pygame.locals
import Track

class Channel:

	def __init__(self, id):
		self._track = None
		self._id = id
		self._pychan = pygame.mixer.Channel(id)
		self._pychan.set_endevent(pygame.locals.USEREVENT)

	def set_track(self, track):
		self._track = track

	def get_track(self):
		return self._track

	def play(self):
		self._pychan.play(self._track.get_sound())
		self._track.add_playing()

	def stop(self):
		self._pychan.stop()
		self._reset()

	def is_busy(self):
		if self._pychan.get_busy():
			return True
		self._reset()
	
	def _reset(self):
		self._track.sub_playing()
		self._track = None

