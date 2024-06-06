import pygame as pg
from  Architect import Building
from Elevator import Elevator
from Floor import Floor
from Manager import call, travels,show_arrival_time
from elevator_selection import elevator_selection
import time
import pygame.mixer
height_floor = 64


background_screen_img = "lobby.png"
screen_color =(255,255,255)
        #initial creation of the background screen and dimensions  
def screen_design(elevators_numbers,floors_number):
    width = (elevators_numbers) * Elevator.width() + Floor.width() + Floor.timer_width()
    height = floors_number * Floor.height() - Floor.black_space_thickness()
    pg.init()
    size = (width,height)
    screen = pg.display.set_mode(size)
    pg.display.set_caption("building_game")
    screen.fill(screen_color)
    # background_screen = pg.image.load(background_screen_img)
    # background_screen = pg.transform.scale(background_screen, (width, height))
    # screen.blit(background_screen,(0,0))
    return screen
    
def main(elevators_numbers,floors_number):
    # if type(elevators_numbers) != int or type(floors_number) != int:
    #    return main(elevators_numbers,floors_number)
    # int(elevators_numbers)
    # int(floors_number)
    
    
    screen = screen_design(elevators_numbers,floors_number)   
    building = Building()
    
       #initial creation of floors and elevators
    building.new_building_architect(floors_number, elevators_numbers, screen) 
    finish = False
    while not finish:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                finish = True              
            #call is function of manager
            call(building,event, screen)
        # show_arrival_time(screen, building)
        # show_time(screen,building)
        travels(screen,building)
        building.close_finish_orders()
        # building.update_elevators_status()     
        pg.display.flip()
        pg.time.Clock().tick(height_floor*2)
     
      
main(5,10)

   

