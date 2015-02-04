
class AbstractCommand:
	def __init__(self, cmanager, key):
		self.cmanager = cmanager
		self.key = key
	def is_this_command(self, key):
		return key == self.key
	def execute(self, tmanager):
		self._exec(tmanager)

class Play (AbstractCommand):
	def __init__(self, cmanager, key):
		AbstractCommand.__init__(self, cmanager, key)
	def _exec(self, tmanager):
		print 'Play'
		for t in tmanager.get_selected_tracks():
			print '   ' + t.get_name()
			self.cmanager.play_track(t)
		tmanager.unselect_all()

class Fadein (AbstractCommand):
	def __init__(self, cmanager, key):
		AbstractCommand.__init__(self, cmanager, key)
	def _exec(self, tmanager):
		print 'Fadein'
		for t in tmanager.get_selected_tracks():
			print '   ' + t.get_name()
			self.cmanager.play_track(t, 2000)
		tmanager.unselect_all()

class Stop (AbstractCommand):
	def __init__(self, cmanager, key):
		AbstractCommand.__init__(self, cmanager, key)
	def _exec(self, tmanager):
		print 'Stop'
		for t in tmanager.get_selected_tracks():
			print '   ' + t.get_name()
			self.cmanager.stop_track(t)
		tmanager.unselect_all()

class Fadeout (AbstractCommand):
	def __init__(self, cmanager, key):
		AbstractCommand.__init__(self, cmanager, key)
	def _exec(self, tmanager):
		print 'Fadeout'
		for t in tmanager.get_selected_tracks():
			print '   ' + t.get_name()
			self.cmanager.stop_track(t, 2000)
		tmanager.unselect_all()

class UpTracks (AbstractCommand):
	def __init__(self, cmanager, key):
		AbstractCommand.__init__(self, cmanager, key)
	def _exec(self, tmanager):
		print 'Up'
		tmanager.add_offset(1)

class DownTracks (AbstractCommand):
	def __init__(self, cmanager, key):
		AbstractCommand.__init__(self, cmanager, key)
	def _exec(self, tmanager):
		print 'Up'
		tmanager.add_offset(-1)

