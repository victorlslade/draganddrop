
#character.Character

import pygame as pg #lazy but responsible (avoid namespace flooding)
import myconstants as mc

class Character:
    def __init__(self,rect):
        self.rect = pg.Rect(rect)
        self.rect = pg.Rect(rect)
        self.click = False
        self.image = pg.Surface(self.rect.size).convert()
        self.image.fill((mc.GREEN))
    def update(self,surface):
        if self.click:
            self.rect.center = pg.mouse.get_pos()
        surface.blit(self.image,self.rect)