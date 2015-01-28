import Track, Manager

def load_playlist(manager, playlist_filename):
	print "Loading playlist '" + playlist_filename + "'"
	with open(playlist_filename, "r") as f:
		content = f.readlines()
		for l in content:
			try:
				track = Track.Track(l.rstrip())
				manager.add(track)				
			except RuntimeError:
				print "Error when loading sound '" + l + "'"
		f.close()

