import Track, Manager, os, pygame

_sounds = {}
_images = {}

def _get_sound_and_image(soundpath, imagepath):
	# sound
	if _sounds.has_key(soundpath):
		print "Reuse '" + soundpath + "'"
		sound = _sounds.get(soundpath)
	else:
		print "Load  '" + soundpath + "'"
		_sounds[soundpath] = pygame.mixer.Sound(soundpath)
		sound = _sounds.get(soundpath)
	# image
	if _images.has_key(imagepath):
		print "Reuse '" + imagepath + "'"
		image = _images.get(imagepath)
	else:
		print "Load  '" + imagepath + "'"
		if os.path.exists(imagepath):
			_images[imagepath] = pygame.image.load(imagepath)
		image = _images.get(imagepath)
	
	return sound, image


def load_playlist(manager, playlist_filename):
	print "Loading playlist '" + playlist_filename + "'"
	with open(playlist_filename, "r") as f:
		content = f.readlines()
		for l in content:
			soundpath = l.rstrip()
			try:
				imagepath = soundpath + ".bmp"

				sound, image = _get_sound_and_image(soundpath, imagepath)
				track = Track.Track(sound, soundpath.split("/")[-1], image)

				manager.add(track)				
			except RuntimeError:
				print "Error when loading sound '" + l + "'"
		f.close()

