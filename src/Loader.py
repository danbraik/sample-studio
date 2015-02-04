import Track, Manager, os

def load_playlist(manager, playlist_filename):
	print "Loading playlist '" + playlist_filename + "'"
	with open(playlist_filename, "r") as f:
		content = f.readlines()
		for l in content:
			l = l.rstrip()
			try:
				track = Track.Track(l)
				image = l + ".bmp"
				if os.path.exists(image):
					track.set_imagepath(image)
				manager.add(track)				
			except RuntimeError:
				print "Error when loading sound '" + l + "'"
		f.close()

