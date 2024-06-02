from Architect import Building

elevators = set()

def dst_arrival_time(dst,elevator):
       return abs(elevator.absolute_stop - dst)/2                           #
    

def get_priority_elevator(dst,building):
    min_possible_time = float('inf')
    for elevator in building.elevators:    
                          #from eli class
        arrival_time = elevator.operation_duration + dst_arrival_time(dst,elevator) - elevator.elapsed_time(building)
        if min_possible_time > arrival_time: 
            min_possible_time = arrival_time
            property__elevator = elevator
    return property__elevator
                              
def elevator_selection(floor,building, screen):
    priority_elevator = get_priority_elevator(floor,building)
    return priority_elevator
     