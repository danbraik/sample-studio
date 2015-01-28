from __future__ import absolute_import
from src import Main
import sys, os

if len(sys.argv) < 2:
	sys.exit('Usage: %s playlist' % sys.argv[0])

if not os.path.exists(sys.argv[1]):
	sys.exit('ERROR: Playlist "%s" was not found!' % sys.argv[1])

Main.run(sys.argv[1])

