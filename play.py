import pygame as pg
from  Architect import Architect
from Elevator import Elevator
from Floor import Floor
from Manager import Manager
import time
height_floor = 64


background_screen_img = "lobby.png"
screen_color =(255,255,255)
        #initial creation of the background screen and dimensions  
def screen_design(elevators_numbers,floors_number, A):
    width = (elevators_numbers) * A.width_elevator + A.floor_width + A.timer_width
    height = floors_number * A.floor_height - A.black_space_thickness
    pg.init()
    size = (width,height)
    screen = pg.display.set_mode(size)
    pg.display.set_caption("manager_game")
    screen.fill(screen_color)
    # background_screen = pg.image.load(background_screen_img)
    # background_screen = pg.transform.scale(background_screen, (width, height))
    # screen.blit(background_screen,(0,0))
    return screen

    
def main(elevators_numbers,floors_number):    
    manager = Manager()
    A = Architect()
    screen = screen_design(elevators_numbers,floors_number, A) 
       #initial creation of floors and elevators
    A.new_building_architect(floors_number, elevators_numbers, screen, manager) 
    start_T = 0
    finish_T = 0
    finish = False
    while not finish:
        sleep_T = finish_T - start_T
        if (1/height_floor) > sleep_T:
            time.sleep(abs((1/height_floor)-sleep_T))
        start_T = time.time()   
        for event in pg.event.get():
            if event.type == pg.QUIT:
                finish = True              
            #call is function of manager
            manager.call(event, screen, A)  
        manager.travels(screen,A)
        manager.update_arrival_time(manager,screen, A)  
        manager.close_finish_orders(manager)    
        pg.display.flip()
        pg.time.Clock().tick(height_floor*4)
        finish_T = time.time()
      
main(1,12)

   

