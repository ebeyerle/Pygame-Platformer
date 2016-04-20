import pygame



class Actor(object):
	def __init__(self, position, speed, size):
		self.position = position
		self.speed = speed
		self.size = size

		self.surface = None

		self.animations = []
		self.current_animation = 0

	def place(self, position):
		self.position = pygame.rect.Rect(position, self.size)
		self.next_position = pygame.rect.Rect(position, self.size)
		print "Here"

	def draw(self, surface):
		(ix, iy) = (int(round(self.position[0])), int(round(self.position[1])))
		frame = self.animations[self.current_animation].current_frame()
		surface.blit(frame, self.position)

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

    #def collide_actor(self, actor):
    #    pass
