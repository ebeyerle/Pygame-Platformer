#    The main code file for Shundread's silly platformer
#    Copyright (C) 2011  Thiago Chaves de Oliveira Horta
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.

from os.path import join

import pygame

import graphics, tile

import test

game_title = "Shundread's silly platformer"


def initialization():
    pygame.init()
    pygame.display.set_mode(graphics.screen_size)
    pygame.display.set_caption(game_title)

    tile.init()

def main():
    initialization()

    #test.animate("data/sprites/hero.png", (128, 128), range(1, 5), 100)
    test.collision()
