import pygame as pg
from  Architect import Architect
from Manager import Manager
import time

        #initial creation of the background screen and dimensions  
def screen_design(elevators_numbers,floors_number, A):
    width = (elevators_numbers) * A.width_elevator + A.floor_width + A.timer_width
    height = floors_number * A.floor_height - A.black_space_thickness
    pg.init()
    size = (width,height)
    screen = pg.display.set_mode(size)
    pg.display.set_caption("manager_game")
    screen.fill(A.screen_color)
    return screen

    
def main(elevators_numbers,floors_number):    
    manager = Manager()
    A = Architect()
       #initial creation of the background screen and dimensions 
    screen = screen_design(elevators_numbers,floors_number, A) 
       #initial creation of floors and elevators
    A.new_building_architect(floors_number, elevators_numbers, screen, manager) 
    #Reset clock for first iteration
    start_T = 0
    finish_T = 0
    #The game loop
    finish = False
    while not finish:
        #The duration of the iteration
        sleep_T = finish_T - start_T
        # Maintaining the rate of iterations per second
        if (1/A.floor_height) > sleep_T:
            time.sleep(abs((1/A.floor_height)-sleep_T))
        start_T = time.time()  
        #Game closing conditions 
        for event in pg.event.get():
            if event.type == pg.QUIT:
                finish = True              
            #Making an order (including order confirmation and updating the status of floors and elevators)
            manager.call(event, screen, A) 
        # The elevator transport     
        manager.travels(screen,A)
        # Countdown display
        manager.update_arrival_time(manager,screen, A)  
        # Closing the reservation and updating the elevator status
        manager.close_finish_orders(manager)    
        pg.display.flip()
        pg.time.Clock().tick(A.floor_height*4)
        finish_T = time.time()
      
main(3,12)

   

