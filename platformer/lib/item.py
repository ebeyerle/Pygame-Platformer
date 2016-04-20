import pygame

import graphics

width = 32
height = 32
size = (width, height)

frame_duration = 80


class Item(object):
        def __init__(self):
                #position, speed, size
                self.position = None
                self.size = size
                self.item = pygame.image.load("item.png")


        def place(self, position):
                self.position = pygame.rect.Rect(position, self.size)
                self.next_position = pygame.rect.Rect(position, self.size)

        def draw(self, surface):
                surface.blit(self.item, self.position)

        def calculate_next_position(self):
                self.next_position.topleft = (self.position[0] + self.speed[0], self.position[1] + self.speed[1])

        def set_next_position(self, new_position):
                self.position = new_position

        def collide_wall(self):
                pass

        def collide_actor(self, actor):
                pass
