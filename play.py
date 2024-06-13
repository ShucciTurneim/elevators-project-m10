import pygame as pg
from Manager import Manager
from Data_base import *
import time


        #initial creation of the background screen and dimensions 
def screen_design(elevators_numbers,floors_number):
    width = (elevators_numbers) * width_elevator + floor_width + timer_width
    height = floors_number * floor_height - black_space_thickness
    pg.init()
    size = (width,height)
    screen = pg.display.set_mode(size)
    pg.display.set_caption("building_game")
    screen.fill(screen_color)
    return screen

    
def main(elevators_numbers,floors_number):    
    manager = Manager()
       #initial creation of the background screen and dimensions 
    screen = screen_design(elevators_numbers,floors_number) 
       #initial creation of floors and elevators
    manager.new_building_architect(floors_number, elevators_numbers, screen) 
    #Reset clock for first iteration
    start_T = 0
    finish_T = 0
    #The game loop
    finish = False
    while not finish:
        #The duration of the iteration
        sleep_T = finish_T - start_T
        # Maintaining the rate of iterations per second
        if (1/floor_height) > sleep_T:
            time.sleep(abs((1/floor_height)-sleep_T))
        start_T = time.time()  
        #Game closing conditions 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                finish = True              
            #Making an order (including order confirmation and updating the status of floors and elevators)
            manager.call(event, screen) 
        # The elevator transport     
        manager.travels(screen)
        # Countdown display
        manager.update_arrival_time(manager,screen)  
        # Closing the reservation and updating the elevator status
        manager.close_finish_orders()    
        pg.display.flip()
        pg.time.Clock().tick(floor_height*2)
        finish_T = time.time()
      
main(1,12)

   

