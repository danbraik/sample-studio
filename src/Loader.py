
import Sound, Track, Manager


def load_playlist(manager, playlist_filename):
	print "Loading playlist '" + playlist_filename + "'"
	with open(playlist_filename, "r") as f:
		content = f.readlines()
		for l in content:
			try:
				sound = Sound.Sound(l.rstrip())
				track = Track.Track(sound)
				manager.add(track)				
			except Error:
				print "Error when loading sound '" + l + "'"
		f.close()
