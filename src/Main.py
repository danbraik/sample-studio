import sys, pygame
import pygame.locals
import Track, TManager, Selection, Loader, Color
import Commands, DrawText, Channel, CManager


ressources_dir = "ressources/"


def quit():
	pygame.quit()
	sys.exit()


def run(playlist_file):
	# Init pygame
	pygame.mixer.pre_init(44100, -16, 2, 2048) # setup mixer to avoid sound lag
	print "Init pygame, version = ", pygame.version.ver
	
	pygame.init()
	if not pygame.display.get_init():
		print "Error during pygame init."
		print "Quit."
		sys.exit(1)
	
	
	# Init Screen
	fullscreen = False
	size = width, height = 1366/ (1 if fullscreen else 2),768/ (1 if fullscreen else 2)
	
	screen = pygame.display.set_mode(size, (pygame.FULLSCREEN | pygame.HWSURFACE if fullscreen else pygame.RESIZABLE))
	pygame.display.set_caption("Ardent'Scene studio")
	pygame.mouse.set_visible(False)

	# Init modules
	DrawText.init()
	
	# Init entities
	ball = pygame.image.load(ressources_dir + "ball.gif")
	ballrect = ball.get_rect()
	speed = [20, 18]


	# ***
	tmanager = TManager.Manager()
	cmanager = CManager.CManager()

	Loader.load_playlist(tmanager, playlist_file)

	keys = [pygame.K_a, pygame.K_z, pygame.K_e,
			pygame.K_r, pygame.K_t, 
			pygame.K_y, pygame.K_u, pygame.K_i,
			pygame.K_o, pygame.K_p]
	selection = Selection.Selection(tmanager, keys, pygame.K_ASTERISK)
	
	commands = [
			Commands.Play(tmanager, cmanager, pygame.K_b),
			Commands.Stop(tmanager, cmanager, pygame.K_n),
			Commands.Fadein(tmanager, cmanager, pygame.K_h),
			Commands.Fadeout(tmanager, cmanager, pygame.K_j),
			Commands.UpTracks(tmanager, cmanager, pygame.K_UP),
			Commands.DownTracks(tmanager, cmanager, pygame.K_DOWN)
			]

	# to know when exiting the soft
	quitting = 0

	while 1:
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT: 
	        	quit()
	        # ---
	        elif event.type == pygame.KEYDOWN:
	        	quitting = quitting-1
	        	if event.key == pygame.K_ESCAPE:
	        		quit()
	        	elif event.key == pygame.K_BACKSPACE:
	        		if quitting < 0:
	        			quitting = 0
	        		quitting = quitting + 2
	        		if quitting >= 5:
	        			quit()
	        	elif event.key == pygame.K_SPACE:
	        		None
	        	# select a track
	        	elif selection.is_selection(event.key):
	        		selection.treat_key(event.key)
	        	# execute a command
	        	else:
	        		for cmd in commands:
	        			if cmd.is_this_command(event.key):
	        				cmd.execute()
	        # ---
	        elif event.type == pygame.locals.USEREVENT:
	        	print 'Event : Sound has finished'
	        	# Channel event
	        	cmanager.has_finished()
	
	    ballrect = ballrect.move(speed)
	    if ballrect.left < 0 or ballrect.right > width:
	        speed[0] = -speed[0]
	    if ballrect.top < 0 or ballrect.bottom > height:
	        speed[1] = -speed[1]
	
	    screen.fill(Color.black)
	    screen.blit(ball, ballrect)
	    tmanager.draw(screen)
	    pygame.display.flip()
	    pygame.time.delay(50)
	
	
