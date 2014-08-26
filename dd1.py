import os,sys
import pygame as pg #lazy but responsible (avoid namespace flooding)
# character.py in this directory? a module?
import character



def main(Surface,Player):
    game_event_loop(Player)
    Surface.fill(0)
    Player.update(Surface)
def game_event_loop(Player):
    for event in pg.event.get():
        if event.type == pg.MOUSEBUTTONDOWN:
            if Player.rect.collidepoint(event.pos):
                Player.click = True
        elif event.type == pg.MOUSEBUTTONUP:
            Player.click = False
        elif event.type == pg.QUIT:
            pg.quit(); sys.exit()

if __name__ == "__main__":
    os.environ['SDL_VIDEO_CENTERED'] = '1'
    pg.init()
    Screen = pg.display.set_mode((1000,600))
    MyClock = pg.time.Clock()
    MyPlayer =character.Character((0,0,150,30))
    MyIcon = character.Character((300,0,150,30))

    #MyPlayer.rect.center = Screen.get_rect().center
    while 1:
        main(Screen,MyPlayer)
        pg.display.update()
        MyClock.tick(60)