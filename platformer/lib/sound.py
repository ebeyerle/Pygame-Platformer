import pygame

class Sound(object):
  def __init__(self, n):
    self.name = n
    self.sound = pygame.mixer.Sound(self.name) 

  def play(self):
    self.sound.play()

  def stop(self):
    self.sound.stop()

  def incr(self):
    v = self.sound.get_volume()
    self.sound.set_volume(v+10)

