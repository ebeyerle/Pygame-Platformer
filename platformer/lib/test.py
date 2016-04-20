from os.path import join
import pygame
import room
import player
#import player1
import graphics
import tile

game_title = "Python Platformer"

#Testing this section###########################################
def initialization():
	pygame.init()
	pygame.display.set_mode(graphics.screen_size)
	pygame.display.set_caption(game_title)

	tile.init()
################################################################
def game_run():
	pygame.event.set_blocked(None)
	pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])

	screen = pygame.display.get_surface()
	screen_rect = screen.get_rect()

	p = player.Player()
	p.place((200, 200))

	r = room.load("sample room2.txt")

	clock = pygame.time.Clock()
	dt = 0
	while True:
		# Handle quitting
		if pygame.event.get(pygame.QUIT):
			return

		# Handle player input
		key_presses = pygame.event.get(pygame.KEYDOWN)
		key_states = pygame.key.get_pressed()

		# Get the actors' new positions
		actors = [p]
		for a in actors:
			a.update(dt, key_states, key_presses)
			a.calculate_next_position()

		for a in actors:
			p0 = a.position
			p1 = a.next_position

			# Collision actor-wall version 3
			tp = pygame.rect.Rect(p1)

			x, y = 1, 1
			tiles = r.tiles_around(p0.center)
			# Test bottom
			if tiles[x][y+1] and tiles[x][y+1][1].solid and tp.colliderect(tiles[x][y+1][0]):
				tp.bottom = tiles[x][y+1][0].top
				a.speed[1] = 0
			# Test top
			if tiles[x][y-1] and tiles[x][y-1][1].solid and tp.colliderect(tiles[x][y-1][0]):
				tp.top = tiles[x][y-1][0].bottom
				a.speed[1] = 0
			# Test left
			if tiles[x-1][y] and tiles[x-1][y][1].solid and tp.colliderect(tiles[x-1][y][0]):
				tp.left = tiles[x-1][y][0].right
				a.collide_wall()
			# Test right
			if tiles[x+1][y] and tiles[x+1][y][1].solid and tp.colliderect(tiles[x+1][y][0]):
				tp.right = tiles[x+1][y][0].left+1
				a.collide_wall()
            
			for e in key_presses:
				if e.key == pygame.K_SPACE:
					print tp.topleft, tp.bottomright
					for y in range(3):
						for x in range(3):
 							print tiles[x][y][0].topleft,
						print

			a.set_next_position(tp)

		# Collision player-mobs version 1
		#for m in mobs:
		#    if p.position.colliderect(m.position):
		#        print "Boing"

		# Draw stuff
		r.draw(screen)
		p.draw(screen)
		#for m in mobs:
		#    m.draw(screen)

		pygame.display.flip()
		dt = clock.tick(15)

if __name__ == "__main__":
	initialization()
	print "Start of game"
	game_run()

