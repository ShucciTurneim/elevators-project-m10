import pygame as pg
from  Architect import new_building_architect
from Elevator import Elevator

# width = 600
# hight = 600
white =(255,255,255)

elevators_numbers = int(input("enter elevators integer number"))
floors_number = int(input("enter floors integer number"))
def main(elevators_numbers,floors_number):
    # if type(elevators_numbers) != int or type(floors_number) != int:
    #    return main(elevators_numbers,floors_number)
    # int(elevators_numbers)
    # int(floors_number)
    width = (elevators_numbers + 2) * 64
    hight = floors_number * 64
    pg.init()
    size = (width,hight)
    screen = pg.display.set_mode(size)
    pg.display.set_caption("building_game")
    screen.fill(white)
    pg.display.flip()
    # image ="/home/mefathim/Documents/elevators-project-m10/elv.png"
    # IMAGE_SMALL = pg.transform.scale(image,(50, 30))
    # img = pg.image.lo
    new_building_architect(floors_number, elevators_numbers,screen)



    finish = False
    while not finish:
      for event in pg.event.get():
        if event.type == pg.QUIT:
            finish = True
# pg.quit()
main(elevators_numbers,floors_number)
   

