
def dst_arrival_time(dst,elevator):
       return abs(elevator.absolute_stop - dst)/2                           #
    

def elevator_selection(floor,building,screen):
    dst = floor.number
    min_possible_time = float('inf')
    for elevator in building.elevators:    
        arrival_time = elevator.operation_duration + dst_arrival_time(dst,elevator) - elevator.elapsed_time(building)
        if min_possible_time > arrival_time: 
            min_possible_time = arrival_time
            priority_elevator = elevator
    floor.request_in_process(min_possible_time,screen)
    priority_elevator.send_order(dst)
                              

    
     