from __future__ import absolute_import
from src import Main
import sys, os

if len(sys.argv) < 2:
	sys.exit('Usage: %s playlist...' % sys.argv[0])
# rm program name
sys.argv.pop(0)

Main.run(sys.argv)

