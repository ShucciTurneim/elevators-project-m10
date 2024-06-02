import pygame as pg
from  Architect import Building
from Elevator import Elevator
from Floor import Floor
from Manager import call

background_screen_img = "/home/mefathim/Documents/elevators-project-m10/lobby.png"
screen_color =(255,255,255)

def screen_design(elevators_numbers,floors_number):
    width = (elevators_numbers) * Elevator.width() + Floor.width() + Floor.timer_width()
    height = floors_number * Floor.height() - Floor.black_space_thickness()
    pg.init()
    size = (width,height)
    screen = pg.display.set_mode(size)
    pg.display.set_caption("building_game")
    screen.fill(screen_color)
    background_screen = pg.image.load(background_screen_img)
    background_screen = pg.transform.scale(background_screen, (width, height))
    screen.blit(background_screen,(0,0))
    return screen
    
def main(elevators_numbers,floors_number):
    # if type(elevators_numbers) != int or type(floors_number) != int:
    #    return main(elevators_numbers,floors_number)
    # int(elevators_numbers)
    # int(floors_number)
    screen = screen_design(elevators_numbers,floors_number)

    pg.display.flip()
    building = Building()
    building.new_building_architect(floors_number, elevators_numbers, screen)
    
    finish = False
    while not finish:
      for event in pg.event.get():
        if event.type == pg.QUIT:
            finish = True
        left = 1    
        if event.type == pg.MOUSEBUTTONDOWN and event.button  == left:
            mouse_position = pg.mouse.get_pos() 
            call(mouse_position,floors_number,building,screen) 
            
            
# pg.quit()
main(2,10)

   

