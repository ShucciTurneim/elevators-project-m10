import pygame as pg


width = 600
hight = 600
white =(255,255,255)
pg.init()
size = (width,hight)
screen = pg.display.set_mode(size)
pg.display.set_caption("game")
screen.fill(white)
pg.display.flip()
image ="/home/mefathim/Documents/elevators-project-m10/elv.png"
# IMAGE_SMALL = pg.transform.scale(image,(50, 30))
img = pg.image.load(image)
screen.blit(img,(0,hight-64))
pg.display.flip()



finish = False
while not finish:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            finish = True
# pg.quit()
   

