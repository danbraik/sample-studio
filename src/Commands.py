
class AbstractCommand:
	def __init__(self, tmanager, cmanager, key):
		self.tmanager = tmanager
		self.cmanager = cmanager
		self.key = key
	def is_this_command(self, key):
		return key == self.key
	def execute(self):
		self._exec()

class Play (AbstractCommand):
	def __init__(self, tmanager, cmanager, key):
		AbstractCommand.__init__(self, tmanager, cmanager, key)
	def _exec(self):
		print 'Play'
		for t in self.tmanager.get_selected_tracks():
			print '   ' + t.get_name()
			self.cmanager.play_track(t)
		self.tmanager.unselect_all()

class Fadein (AbstractCommand):
	def __init__(self, tmanager, cmanager, key):
		AbstractCommand.__init__(self, tmanager, cmanager, key)
	def _exec(self):
		print 'Fadein'
		for t in self.tmanager.get_selected_tracks():
			print '   ' + t.get_name()
			self.cmanager.play_track(t, 2000)
		self.tmanager.unselect_all()

class Stop (AbstractCommand):
	def __init__(self, tmanager, cmanager, key):
		AbstractCommand.__init__(self, tmanager, cmanager, key)
	def _exec(self):
		print 'Stop'
		for t in self.tmanager.get_selected_tracks():
			print '   ' + t.get_name()
			self.cmanager.stop_track(t)
		self.tmanager.unselect_all()

class Fadeout (AbstractCommand):
	def __init__(self, tmanager, cmanager, key):
		AbstractCommand.__init__(self, tmanager, cmanager, key)
	def _exec(self):
		print 'Fadeout'
		for t in self.tmanager.get_selected_tracks():
			print '   ' + t.get_name()
			self.cmanager.stop_track(t, 2000)
		self.tmanager.unselect_all()

class UpTracks (AbstractCommand):
	def __init__(self, tmanager, cmanager, key):
		AbstractCommand.__init__(self, tmanager, cmanager, key)
	def _exec(self):
		print 'Up'
		self.tmanager.offset += 1

class DownTracks (AbstractCommand):
	def __init__(self, tmanager, cmanager, key):
		AbstractCommand.__init__(self, tmanager, cmanager, key)
	def _exec(self):
		print 'Up'
		self.tmanager.offset -= 1
