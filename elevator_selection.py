
def dst_arrival_time(dst,elevator):
       return abs(elevator.absolute_stop - dst)/2                           #
    

def elevator_selection(dst,building):
    min_possible_time = float('inf')
    for elevator in building.elevators:    
        arrival_time = elevator.operation_duration + dst_arrival_time(dst,elevator) - elevator.elapsed_time(building)
        if min_possible_time > arrival_time: 
            min_possible_time = arrival_time
            priority_elevator = elevator
    # building.floors[dst].time_left = min_possible_time
    priority_elevator.send_order(dst)
                              

    
     