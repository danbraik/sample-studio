
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
			print '   ' + t.get_name()
			#t.play()
		self.manager.unselect_all()


class Fadein (AbstractCommand):

	def __init__(self, manager, key):
		AbstractCommand.__init__(self, manager, key)
	
	def _exec(self):
		print 'Fadein'
		for t in self.manager.get_selected_tracks():
			print '   ' + t.get_name()
			#t.get_sound().fadein()
		self.manager.unselect_all()



class Stop (AbstractCommand):

	def __init__(self, manager, key):
		AbstractCommand.__init__(self, manager, key)
	
	def _exec(self):
		print 'Stop'
		for t in self.manager.get_selected_tracks():
			print '   ' + t.get_name()
			t.get_sound().stop()
		self.manager.unselect_all()


class Fadeout (AbstractCommand):

	def __init__(self, manager, key):
		AbstractCommand.__init__(self, manager, key)
	
	def _exec(self):
		print 'Fadeout'
		for t in self.manager.get_selected_tracks():
			print '   ' + t.get_name()
			t.get_sound().fadeout()
		self.manager.unselect_all()


