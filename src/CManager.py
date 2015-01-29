import pygame
import Channel

# Channel manager

class CManager:

	def __init__(self):
		self._alloc_channels = []
		self._free_channels = []
		for i in range(0, pygame.mixer.get_num_channels()):
			self._free_channels.append(Channel.Channel(i))

	def play_track(self, track):
		chan = self._alloc_a_free_channel(track)
		chan.play()

	def _alloc_a_free_channel(self, track):
		if len(self._free_channels) == 0:
			chan = self._alloc_channels.pop()
			chan.stop()
			self._free_channels.append(chan)
		chan = self._free_channels.pop()
		chan.set_track(track)
		self._alloc_channels.insert(0, chan)
		return chan

	def has_finished(self):
		finished_c = None
		for c in self._alloc_channels:
			if not c.is_busy():
				finished_c = c
		if finished_c != None:
			self._alloc_channels.remove(finished_c)
			self._free_channels.append(finished_c)

