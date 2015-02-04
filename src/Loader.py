import Track, TManager, os, pygame

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
		if os.path.exists(imagepath):
			print "Load  '" + imagepath + "'"
			_images[imagepath] = pygame.image.load(imagepath)
		else:
			print "Skip  '" + imagepath + "'"
		image = _images.get(imagepath)
	
	return sound, image


def _load_playlist(manager, playlist_filename):
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

def load_playlists(playlist_filenames):
	tmans = []

	for playlist in playlist_filenames:
		if not os.path.exists(playlist):
			print('ERROR: Playlist "%s" was not found!' % sys.argv[1])
		else:
			tmanager = TManager.Manager()
			_load_playlist(tmanager, playlist)
			tmans.append(tmanager)
	
	print str(len(tmans)) + " playlists loaded."
	return tmans


