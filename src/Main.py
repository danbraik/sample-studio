import sys, pygame
import Sound, Track, Manager, Selection

ressources_dir = "ressources/"

def run():
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
	speed = [2, 2]
	
	red = (255,0,0)
	green = (0,255,0)
	blue = (0,0,255)
	darkBlue = (0,0,128)
	white = (255,255,255)
	black = (0,0,0)
	pink = (255,200,200)
	yellow = (255,255,0)
	
	myfont = pygame.font.SysFont("monospace", 15)
	label = myfont.render("Some text!", 1, yellow)
	
	#sound0 = pygame.mixer.Sound("sounds/ambiance_pluie_orage.ogg")
	#sound0 = pygame.mixer.Sound("sounds/scene_01_music_JS-Bach-Toccata.ogg")
	sound0 = Sound.Sound("sounds/thunder.ogg")

	track0 = Track.Track(sound0)

	manager = Manager.Manager()
	for i in range(0,5):
		manager.add(Track.Track(sound0))

	keys = [pygame.K_a, pygame.K_z, pygame.K_e,
			pygame.K_r, pygame.K_t, 
			pygame.K_y, pygame.K_u, pygame.K_i,
			pygame.K_o, pygame.K_p]
	selection = Selection.Selection(manager, keys, pygame.K_ASTERISK)
	
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
	        		label = myfont.render("Hello", 0, white)
	        		track0.get_sound().play()
	        	# select a track
	        	elif selection.is_selection(event.key):
	        		print 'select track'
	        		selection.treat_key(event.key)
	
	    ballrect = ballrect.move(speed)
	    if ballrect.left < 0 or ballrect.right > width:
	        speed[0] = -speed[0]
	    if ballrect.top < 0 or ballrect.bottom > height:
	        speed[1] = -speed[1]
	
	    screen.fill(black)
	    pygame.draw.rect(screen, darkBlue, (10,20,100,50), 0)
	    screen.blit(ball, ballrect)
	    #drawHouse(300,300,100,100,screen, pink)
	    manager.draw(screen)
	    screen.blit(label, (100, 100))
	    pygame.display.flip()
	    pygame.time.delay(50)
	
	
	
	def drawHouse(x, y, width, height, screen, color):
		points = [(x,y- ((2/3.0) * height)), (x,y), (x+width,y), (x+width,y-(2/3.0) * height), 
		    		        (x,y- ((2/3.0) * height)), (x + width/2.0,y-height), (x+width,y-(2/3.0)*height)]
		lineThickness = 2
		pygame.draw.lines(screen, color, False, points, lineThickness)
