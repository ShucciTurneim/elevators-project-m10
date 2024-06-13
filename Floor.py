import pygame as pg
import time
from Data_base import *

class Floor:
    def __init__(self, number):
        # variables of creating floor
        self.number = number
        self.roof_position = None
        self.button = ()
        self.button_radius = ()
            
        # variables of call
        self.time_left = 0.0
        self.made_order = False
        self.clock_position = 0
        self.timer_Rect = 0
        self.start_clock = 0

        # Determination location of floor and accessories for each floor.
    def design(self,num_floor,screen_height):
        self.roof_position = screen_height - (num_floor+1) * floor_height     #Position on the Y axis
        #Button dimensions and placement
        width_button_position = floor_width_position + floor_width_img/2
        height_button_position = self.roof_position + black_space_thickness +floor_height_img/2
        self.button = width_button_position,height_button_position
        self.button_radius = floor_height_img//2.5
        #Clock dimensions and placement
        self.clock_position = (floor_width_img/4,self.roof_position + black_space_thickness + floor_height_img/4)
        Clock_rectangle_dimensions = 0,self.roof_position + black_space_thickness, timer_width, floor_height_img   
        self.timer_Rect = pg.Rect(Clock_rectangle_dimensions)
         
    
    def drew_floor_number(self, screen, color):
        font = pg.font.Font(None, int(floor_height_img/2)) 
        number = font.render(f'{self.number}', True, color)
        text_rect = number.get_rect()
        text_rect.center = (self.button)
        screen.blit(number, text_rect)

        
    # a function to draw the button in the center of the floor image
    def drew_button(self, screen, called_by):
        if called_by in (builder,order_completed):     # Default mode
            color = button_default_color
            color_number = numbers_default_color
        else:                                           # Order mode
            color =  button_on_hold_color  
            color_number = numbers_on_hold_color  
        pg.draw.circle(screen, color, self.button, self.button_radius)
        self.drew_floor_number(screen, color_number)


    # Black space drawing
    def drew_roof(self, screen):
        line_center = self.roof_position+black_space_thickness /2
        line_left_position = [floor_width_position, line_center]
        line_right_position = [floor_right_side, line_center]
        pg.draw.line(screen, black_space_color, line_left_position, line_right_position, black_space_thickness)


    #Determining dimensions and building a roof and a button floor
    def build_floor(self, num_floor, screen, screen_height):
        self.design(num_floor,screen_height)
        screen.blit(FLOOR_IMAGE, (floor_width_position, self.roof_position + black_space_thickness ))
        self.drew_button(screen, builder)
        self.drew_roof(screen)
        
    # #operations of call
    
    def draw_timer_display(self,screen,turn_on):
        if turn_on:    
            pg.draw.rect(screen, black_space_color, self.timer_Rect)
            font = pg.font.Font(None, int(floor_height_img/2)) 
            print_format = int(self.time_left*10)/10                               #Limit number of digits to display
            number = font.render(f'{print_format}', True, button_on_hold_color)
            screen.blit(number, self.clock_position)        
        else:
            pg.draw.rect(screen, screen_color, self.timer_Rect) 


    #Initializing order data, coloring a button and displaying order duration
    def request_in_process(self,arrival_time,screen):
        self.time_left = arrival_time
        self.start_clock = time.time()
        self.drew_button(screen, order)
        self.draw_timer_display(screen,True)
     
     
     # Closing an order: (including button color) and Deleting a timer
    def finished_order(self, screen):
        self.made_order = False
        self.draw_timer_display(screen,False)
        self.drew_button(screen, order_completed) 
     
     
     # Update remaining time and order status. (including button color) and displaying them on a screen
    def display_clock(self, screen):
        if self.made_order:
            current_time = time.time()
            self.time_left -= (current_time - self.start_clock)        # Elapsed time reduction
            self.start_clock = time.time()                             # Clock reset
            self.draw_timer_display(screen,True)
            if  self.time_left <= 0.0:
                self.finished_order(screen)