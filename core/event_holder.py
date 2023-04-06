import pygame as pg
from pygame.locals import *
from pygame.rect import FRect
from pygame.math import Vector2

class EventHolder :
    def __init__( self ) :
        self.pressed_keys = []
        self.released_keys = []
        self.held_keys = []

        self.mouse_moved = False
        self.mouse_pos = Vector2(0, 0)
        self.mouse_pressed_keys = [False, False, False]
        self.mouse_released_keys = [False, False, False]
        self.mouse_held_keys = [False, False, False]
        self.mouse_focus = False

        self.should_quit = False
        self.determined_fps = 60
        self.final_fps = 0

    @property
    def mouse_rect( self ) -> FRect:
        return FRect(self.mouse_pos.x - 1, self.mouse_pos.y - 1,2,2)

    def get_events( self ) :
        self.pressed_keys.clear()
        self.released_keys.clear()
        self.mouse_pressed_keys = [False, False, False]
        self.mouse_released_keys = [False, False, False]
        self.mouse_focus = pg.mouse.get_focused()
        self.mouse_moved = False

        for i in pg.event.get() :
            if i.type == WINDOWENTER or MOUSEMOTION :
                self.mouse_pos = Vector2(pg.mouse.get_pos())

            if i.type == QUIT or i.type == KEYDOWN and i.key == K_ESCAPE:
                self.should_quit = True

            if i.type == MOUSEMOTION :
                self.mouse_moved = True

            if i.type == KEYDOWN :
                self.pressed_keys.append(i.key)
                if i.key not in self.held_keys :
                    self.held_keys.append(i.key)

            if i.type == KEYUP :
                self.released_keys.append(i.key)
                if i.key in self.held_keys :
                    self.held_keys.remove(i.key)

            if i.type == MOUSEBUTTONDOWN :
                self.mouse_pressed_keys = list(pg.mouse.get_pressed())
                self.mouse_held_keys = list(pg.mouse.get_pressed())

            if i.type == MOUSEBUTTONUP :
                self.mouse_released_keys = list(pg.mouse.get_pressed())
                self.mouse_held_keys = list(pg.mouse.get_pressed())
