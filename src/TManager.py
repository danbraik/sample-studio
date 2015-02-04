import pygame
import Track
import DrawText

class Manager:

	def __init__(self):
		self.track_surface = pygame.Surface((Track.WIDTH, Track.HEIGHT))
		self.tracks = []
		self.offset = 0
	
	def add(self, track):
		self.tracks.append(track)

	# make a track as selected
	def toggle_selection(self, index):
		if index < len(self.tracks):
			state = self.tracks[index].is_selected()
			self.tracks[index].set_selected(not state)

	def toggle_selection_all(self):
		noneSelected = True
		for t in self.tracks:
			if t.is_selected():
				noneSelected = False
				t.set_selected(False)
		if noneSelected:
			for t in self.tracks:
				t.set_selected(True)

	def get_selected_tracks(self):
		sel_tracks = []
		for t in self.tracks:
			if t.is_selected():
				sel_tracks.append(t)
		return sel_tracks
		
	def unselect_all(self):
		for t in self.tracks:
			t.set_selected(False)

	def add_offset(self, val):
	    new_val = self.offset + val
	    if 0 <= new_val and new_val < len(self.tracks):
	        self.offset = new_val
	
	def get_offset(self):
	    return self.offset

	def draw(self, surface):
		dest_rect = pygame.Rect(10, 50 - (10+Track.HEIGHT)*self.offset, Track.WIDTH, Track.HEIGHT)
		num=0
		for t in self.tracks:
			t.draw(self.track_surface, num)
			surface.blit(self.track_surface, dest_rect)
			dest_rect.move_ip(0, Track.HEIGHT + 10)
			num=num+1
			



