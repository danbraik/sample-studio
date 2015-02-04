

class Selection:

	# keys: ordered keys to be associated to numeric value
	# e.g. passing ['q','w','e'] will result in [q:0,w:1,e2]
	# master: all_tracks
	def __init__(self, keys, master):
		self.keys = keys
		self.master = master

	# know if a key is used to select
	def is_selection(self, key):
		return (key in self.keys) or (key == self.master)

	# call this only if 'is_selection' is true
	def treat_key(self, key, tmanager):
		if key == self.master:
			tmanager.toggle_selection_all()
		else:
			num = self.keys.index(key) + tmanager.get_offset()
			tmanager.toggle_selection(num)
		
