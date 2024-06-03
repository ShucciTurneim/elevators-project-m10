from Architect import Building

elevators = set()

def dst_arrival_time(dst,elevator):
       return abs(elevator.absolute_stop - dst)/2                           #
    

def elevator_selection(dst,building):
    min_possible_time = float('inf')
    for elevator in building.elevators:    
        arrival_time = elevator.operation_duration + dst_arrival_time(dst,elevator) - elevator.elapsed_time(building)
        if min_possible_time > arrival_time: 
            min_possible_time = arrival_time
            property__elevator = elevator
    return property__elevator, min_possible_time
                              

    
     