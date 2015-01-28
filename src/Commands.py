
class AbstractCommand:

	def __init__(self, manager, key):
		self.manager = manager
		self.key = key

	def is_this_command(self, key):
		return key == self.key

	def execute(self):
		self._exec()


class Play (AbstractCommand):

	def __init__(self, manager, key):
		AbstractCommand.__init__(self, manager, key)
	
	def _exec(self):
		print 'Play'
		for t in self.manager.get_selected_tracks():
			print '   ' + t.get_sound().get_name()
			t.get_sound().play()
		self.manager.unselect_all()


