from os.path import join

import pygame

import graphics
from sound import Sound


width = 32
height = 32
size = (width, height)


run_speed = float(width*5) / 1200
fall_accel = float(height/2) / 1000
jump_force = height/3

frame_duration = 100


DELAY = 20
MIN_WALK = 3.0


#Player coordinates
position = None
speed = (0,0)

class Player(object):
	def __init__(self):
		# Position information
		self.position = position
		self.speed = speed
		self.size = size

		self.surface = None

		self.animations = []
		self.current_animation = 0
		#self.jump_sound = Sound("Jump27.wav")

		# Load graphics
		self.imgList = []
		self.curr_ticks = pygame.time.get_ticks()
		self.delay = 0
		self.index = 0

		# Setting up images
		self.loadImages()
		self.image = self.imgList[0]
		self.standingImage = self.imgList[0]
		self.jump_image = pygame.image.load("player_jump.png")
		self.image_state = 0
		self.imageFlip = 0
		self.__imageFacingLeft = True


	def update(self, dt, key_states, key_presses):

		prev_ticks = self.curr_ticks
		self.curr_ticks = pygame.time.get_ticks()
		ticks = self.curr_ticks - prev_ticks

		self.delay += ((run_speed * ticks) + MIN_WALK)
		if self.delay > DELAY:
			self.index = (self.index + 1) % 5
			self.delay = 0

		self.image = self.imgList[self.index]

		xspeed = 0
		yspeed = self.speed[1]
		self.image_state = 0
		self.imageFlip = 0

		if key_states[pygame.K_LEFT]  :
			xspeed = -run_speed * dt
			self.image_state = 1
			self.imageFlip = 1
			if self.imageFacingLeft():
                                self.flipImage()
		elif key_states[pygame.K_RIGHT] :
			xspeed =  run_speed * dt
			self.image_state = 1
			if not self.imageFacingLeft():
                                self.flipImage()
			

		for k in key_presses:
			if k.key == pygame.K_SPACE:
				if yspeed == 0:
					yspeed = -jump_force
					self.image_state = 2
					#self.jump_sound.play()


		yspeed += fall_accel * dt

		self.speed = [xspeed, yspeed]

	
	def imageFacingLeft(self): return self.__imageFacingLeft

	def flipImage(self):
#		self.__imageFacingLeft = not self.__imageFacingLeft
		self.__imageFacingLeft = not self.__imageFacingLeft
		for x in range(0, len(self.imgList)):
			self.imgList[x] = pygame.transform.flip(self.imgList[x], 1, 0)
		self.standingImage = pygame.transform.flip(self.standingImage, 1, 0)

	def loadImages(self):
		imgMaster = pygame.image.load("playerFrames1.png")
		imgMaster = imgMaster.convert()
		imgSize = (32, 32)
		offset = ((0,0),(32,0),(64,0),(96,0),(128,0))
		for i in range(5):
			tmpImg = pygame.Surface(imgSize)
			tmpImg.blit(imgMaster,(0,0),(offset[i], imgSize))
			transColor = tmpImg.get_at((0,0))
			self.imgList.append(tmpImg)

	def place(self, position):
		self.position = pygame.rect.Rect(position, self.size)
		self.next_position = pygame.rect.Rect(position, self.size)


	def draw(self, surface):
		if self.image_state == 0:
			surface.blit(self.standingImage, self.position)
		elif self.image_state == 1:
			surface.blit(self.image, self.position)
		elif self.image_state == 2:
                        surface.blit(self.jump_image, self.position)
	

	def set_animation(self, animation_id):
		if animation_id != self.current_animation:
			self.animations[animation_id].reset()
		self.current_animation = animation_id

	def calculate_next_position(self):
		self.next_position.topleft = (self.position[0] + self.speed[0], self.position[1] + self.speed[1])

	def set_next_position(self, new_position):
		self.position = new_position

	def collide_wall(self):
		pass

	def loadAnimations(self):
		pass


#  def loadImages(self):
#    imgMaster = pygame.image.load("playerFrames0.png")
#    imgMaster = imgMaster.convert()
#    imgSize = (55, 55)
#    offset = ((0, 0), (55, 0), (110, 0), (165, 0), (220, 0))
#    for i in range(5):
#      tmpImg = pygame.Surface(imgSize)
#      tmpImg.blit(imgMaster, (0, 0), (offset[i], imgSize))
#      transColor = tmpImg.get_at((0, 0))
#      tmpImg.set_colorkey(transColor)
#      self.imgList.append(tmpImg)
