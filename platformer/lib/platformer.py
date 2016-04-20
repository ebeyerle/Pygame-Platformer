from os.path import join
import pygame
import room
import player
import item
import graphics
import tile

from sound import Sound

game_title = "Python Platformer"

####Initialization section######################################
def initialization():
	pygame.init()
	pygame.display.set_mode(graphics.screen_size)
	pygame.display.set_caption(game_title)
	pygame.mixer.init()

	tile.init()
################################################################
def game_run():
        pygame.event.set_blocked(None)
        pygame.event.set_allowed([pygame.QUIT, pygame.KEYDOWN])

        #music = pygame.mixer.music.load("POL-sunset-route-short.wav")
        music = pygame.mixer.music.load("POL-miracle-park-short.wav")
        pygame.mixer.music.play(-1)

	#jump_sound = Sound("Jump27.wav")

        screen = pygame.display.get_surface()
        screen_rect = screen.get_rect()

        p = player.Player()
        p.place((100, 200))

        new_item = item.Item()
        new_item.place((220, 200))

        L = []
        r = room.load("sample room2.txt")
        r2 = room.load("sample room3.txt")

        L.append(r)
        L.append(r2)

        clock = pygame.time.Clock()
        dt = 0
#        while True:
                

	
        while True:
                if pygame.event.get(pygame.QUIT):
                        return


                key_presses = pygame.event.get(pygame.KEYDOWN)
                key_states = pygame.key.get_pressed()

		#if event.key == pygame.K_SPACE:
		#jump_sound.play()
		
                assets = [p] + [new_item]
                p.update(dt, key_states, key_presses)
                p.calculate_next_position()

                for a in assets:
                        p0 = a.position
                        p1 = a.next_position


                        tc = pygame.rect.Rect(p1)

                        x, y = 1, 1
                        tiles = r.tiles_around(p0.center)

                        if tiles[x][y+1] and tiles[x][y+1][1].solid and tc.colliderect(tiles[x][y+1][0]):
                                tc.bottom = tiles[x][y+1][0].top
                                a.speed[1] = 0

                        if tiles[x][y-1] and tiles[x][y-1][1].solid and tc.colliderect(tiles[x][y-1][0]):
                                tc.top = tiles[x][y-1][0].bottom
                                a.speed[1] = 0

                        if tiles[x-1][y] and tiles[x-1][y][1].solid and tc.colliderect(tiles[x-1][y][0]):
                                tc.left = tiles[x-1][y][0].right
                                a.collide_wall()

                        if tiles[x+1][y] and tiles[x+1][y][1].solid and tc.colliderect(tiles[x+1][y][0]):
                                tc.right = tiles[x+1][y][0].left+1
                                a.collide_wall()
            
			

                        a.set_next_position(tc)

		
                if p.position.colliderect(new_item.position):
                        print "You Win!"
                        return
                
		# Draw stuff
		#if p.position.colliderect(new_item.position):
                #        print "You Win!!"
                L[0].draw(screen)
                p.draw(screen)
                new_item.draw(screen)


                pygame.display.flip()
                dt = clock.tick(15)

if __name__ == "__main__":
	initialization()
	game_run()

