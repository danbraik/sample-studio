import pygame
import Track


class TrackManager:

	tracks = []
	track_surface = None

	def __init__(self):
		self.track_surface = pygame.Surface((Track.WIDTH, Track.HEIGHT))
	
	def add(self, track):
		self.tracks.append(track)

	def draw(self, surface):
		dest_rect = pygame.Rect(0, 0, Track.WIDTH, Track.HEIGHT)
		for t in self.tracks:
			t.draw(self.track_surface)
			surface.blit(self.track_surface, dest_rect)
			dest_rect.move_ip(0, Track.HEIGHT)



