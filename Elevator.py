from collections import deque
# import floors
class elevator:
    def __init__(self, number):
     #variables of creating elevator   
        self.number = int
        self.width = 512#pxl
        self.hight = 512
        self.left_side_position = #(left wall + floor_width+timer_width)
        self.right_side_position = self.left_side_position + self.width
        self.elevator_img = "/home/mefathim/Downloads/ElevatorChallenge - Python-20240528T073950Z-001/ElevatorChallenge - Python/elv.png"
   
   
    #variables of elevator travel  
        self.que = deque
        self.absolute_stop = self.que[-1]
        self.departure = 0 #self.que.popleft
        self.next_stop = self.que[0]
        self.operation_duration = 0 #sum of all times of objects in q
        
     #operations of creating elevator
    def build_elevator(self,left_side_new_elevator):
        self.left_side_position = left_side_new_elevator
        self.right_side_position = self.left_side_position + self.width
        initial_location_floor = #floor of screen
        initial_location_ceiling = initial_location_floor + self.hight
        
        
        
        
        
        
        
        #operations of elevator travel
    def send_order(self,floor):
        self.operation_duration += (floor.distance/2)+2 #(abs(floor_number- self.absolute_stop)/2)+2
        self.que.append(floor)
        self.absolute_stop = self.que[-1]
        
    def finish_order (self):
        self.operation_duration -= abs(self.departure - self.next_stop)/2
        self.departure = self.que.extendleft
        self.next_stop = self.que[0]
        
    def elapsed_time(self,):
        return (abs(self.next_stop - self.departure)/2)-floor.timer    
        