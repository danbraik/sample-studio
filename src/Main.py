import sys, pygame
import Sound, Track, Manager, Selection, Loader, Color
import Commands


ressources_dir = "ressources/"


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
	
	screen = pygame.display.set_mode(size, (pygame.FULLSCREEN | pygame.HWSURFACE if fullscreen else 0))
	pygame.display.set_caption("Ardent'Scene studio")
	pygame.mouse.set_visible(False)
	
	# Init entities
	ball = pygame.image.load(ressources_dir + "ball.gif")
	ballrect = ball.get_rect()
	speed = [20, 18]


	# ***
	manager = Manager.Manager()

	Loader.load_playlist(manager, playlist_file)

	keys = [pygame.K_a, pygame.K_z, pygame.K_e,
			pygame.K_r, pygame.K_t, 
			pygame.K_y, pygame.K_u, pygame.K_i,
			pygame.K_o, pygame.K_p]
	selection = Selection.Selection(manager, keys, pygame.K_ASTERISK)
	

	commands = [Commands.Play(manager, pygame.K_b)]


	# to know when exiting the soft
	quitting = 0

	while 1:
	    for event in pygame.event.get():
	        if event.type == pygame.QUIT: 
	        	pygame.quit()
	        	sys.exit()
	        if event.type == pygame.KEYDOWN:
	        	quitting = quitting-1
	        	if event.key == pygame.K_ESCAPE:
	        		sys.exit()
	        	elif event.key == pygame.K_BACKSPACE:
	        		if quitting < 0:
	        			quitting = 0
	        		quitting = quitting + 2
	        		if quitting >= 5:
	        			sys.exit()
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
	
	    ballrect = ballrect.move(speed)
	    if ballrect.left < 0 or ballrect.right > width:
	        speed[0] = -speed[0]
	    if ballrect.top < 0 or ballrect.bottom > height:
	        speed[1] = -speed[1]
	
	    screen.fill(Color.black)
	    screen.blit(ball, ballrect)
	    manager.draw(screen)
	    pygame.display.flip()
	    pygame.time.delay(50)
	
	
